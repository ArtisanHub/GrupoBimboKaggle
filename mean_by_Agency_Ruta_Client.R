library(data.table)

#read training data
train <- fread('/home/prashan/Desktop/DM/Kaggle/data/train.csv', select = c('Semana', 'Agencia_ID', 'Canal_ID', 'Ruta_SAK', 'Cliente_ID', 'Producto_ID', 'Demanda_uni_equil'))
test <- fread('/home/prashan/Desktop/DM/Kaggle/data/test.csv', select = c('id', 'Canal_ID' ,'Cliente_ID', 'Producto_ID', 'Agencia_ID', 'Ruta_SAK'))


#transform target variable to log(1 + demand) - this makes sense since we're
#trying to minimize rmsle and the mean minimizes rmse:
#After minizing all rmsle we can get a better answer

train$log_demand = log(train$Demanda_uni_equil+0.000001)
mean_total <- mean(train$log_demand) #overall mean of log_demand

#mean by Canal_ID
mean_C <-  train[, .(MC = mean(log_demand)), by = .(Canal_ID)]
#mean by Canal_ID and ruta
mean_CR <- train[, .(MCR = mean(log_demand)), by = .(Canal_ID, Ruta_SAK)]
#mean by Canal_ID, Ruta_SAK, Producto_ID
mean_CRP <- train[, .(MCRP = mean(log_demand)), by = .(Canal_ID, Ruta_SAK, Producto_ID)]
#mean by Canal_ID, Ruta_SAK, Producto_ID, Cliente_ID
mean_CRPC <- train[, .(MCRPC = mean(log_demand)), by = .(Canal_ID, Ruta_SAK, Producto_ID, Cliente_ID)]

print("Merging means with test set")
submit <- merge(test, mean_CRPC, all.x = TRUE, by = c("Canal_ID", "Ruta_SAK", "Producto_ID","Cliente_ID"))
submit <- merge(submit, mean_CRP, all.x = TRUE, by = c("Canal_ID", "Ruta_SAK", "Producto_ID"))
submit <- merge(submit, mean_CR, all.x = TRUE, by = c("Canal_ID", "Ruta_SAK"))
submit <- merge(submit, mean_C, all.x = TRUE, by = "Canal_ID")

# Now create Predictions column;
submit$Pred <- expm1(submit$MCRPC)
submit[is.na(Pred)]$Pred <- expm1(submit[is.na(Pred)]$MCRP)
submit[is.na(Pred)]$Pred <- expm1(submit[is.na(Pred)]$MCR)
submit[is.na(Pred)]$Pred <- expm1(submit[is.na(Pred)]$MC)
submit[is.na(Pred)]$Pred <- expm1(mean_total)


print("Write out submission file")
# now relabel columns ready for creating submission
setnames(submit,"Pred","Demanda_uni_equil")
# Any results you write to the current directory are saved as output.
write.csv(submit[,.(id,Demanda_uni_equil)],"/home/prashan/Desktop/DM/Kaggle/data/submit_mean.csv", row.names = FALSE)
print("Done!")