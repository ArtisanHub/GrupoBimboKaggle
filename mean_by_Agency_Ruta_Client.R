library(data.table)

#read training data
train <- fread('/home/prashan/Desktop/DM/Kaggle/data/train.csv', select = c('Semana', 'Agencia_ID', 'Canal_ID', 'Ruta_SAK', 'Cliente_ID', 'Producto_ID', 'Demanda_uni_equil'))
test <- fread('/home/prashan/Desktop/DM/Kaggle/data/test.csv', select = c('id','Semana', 'Canal_ID' ,'Cliente_ID', 'Producto_ID', 'Agencia_ID', 'Ruta_SAK'))

train$log_demand = log(train$Demanda_uni_equil+ 0.00001)
median_total <- median(train$log_demand) #overall median of log_demand

#median by Canal_ID
median_C <-  train[, .(MC = median(log_demand)), by = .(Canal_ID)]
#median by Canal_ID and ruta
median_CR <- train[, .(MCR = median(log_demand)), by = .(Canal_ID, Ruta_SAK)]
#median by Canal_ID, Ruta_SAK, Producto_ID
median_CRP <- train[, .(MCRP = median(log_demand)), by = .(Canal_ID, Ruta_SAK, Producto_ID)]
#median by Canal_ID, Ruta_SAK, Producto_ID, Cliente_ID
median_CRPC <- train[, .(MCRPC = median(log_demand)), by = .(Canal_ID, Ruta_SAK, Producto_ID, Cliente_ID)]
#median by Canal_ID, Ruta_SAK, Producto_ID, Cliente_ID, Agencia_ID
median_CRPCA <- train[, .(MCRPCA = median(log_demand)), by = .(Canal_ID, Ruta_SAK, Producto_ID, Cliente_ID, Agencia_ID)]
#median by Canal_ID, Ruta_SAK, Producto_ID, Cliente_ID, Agencia_ID, Semana
median_CRPCAS <- train[, .(MCRPCAS = median(log_demand)), by = .(Canal_ID, Ruta_SAK, Producto_ID, Cliente_ID, Agencia_ID, Semana)]

print("Merging medians with test set")
submit <- merge(test, median_CRPCAS, all.x = TRUE, by = c("Canal_ID", "Ruta_SAK", "Producto_ID","Cliente_ID", "Agencia_ID","Semana"))
submit <- merge(submit, median_CRPCA, all.x = TRUE, by = c("Canal_ID", "Ruta_SAK", "Producto_ID","Cliente_ID", "Agencia_ID"))
submit <- merge(submit, median_CRPC, all.x = TRUE, by = c("Canal_ID", "Ruta_SAK", "Producto_ID","Cliente_ID"))
submit <- merge(submit, median_CRP, all.x = TRUE, by = c("Canal_ID", "Ruta_SAK", "Producto_ID"))
submit <- merge(submit, median_CR, all.x = TRUE, by = c("Canal_ID", "Ruta_SAK"))
submit <- merge(submit, median_C, all.x = TRUE, by = "Canal_ID")

# Now create Predictions column;
submit$Pred <- exp(submit$MCRPCAS) - - 0.00001
submit[is.na(Pred)]$Pred <- exp(submit[is.na(Pred)]$MCRPCA) - 0.00001
submit[is.na(Pred)]$Pred <- exp(submit[is.na(Pred)]$MCRPC) - 0.00001
submit[is.na(Pred)]$Pred <- exp(submit[is.na(Pred)]$MCRP) - 0.00001
submit[is.na(Pred)]$Pred <- exp(submit[is.na(Pred)]$MCR) - 0.00001
submit[is.na(Pred)]$Pred <- exp(submit[is.na(Pred)]$MC) - 0.00001
submit[is.na(Pred)]$Pred <- exp(median_total) - 0.00001


print("Write out submission file")
# now relabel columns ready for creating submission
setnames(submit,"Pred","Demanda_uni_equil")
# Any results you write to the current directory are saved as output.
write.csv(submit[,.(id,Demanda_uni_equil)],"/home/prashan/Desktop/DM/Kaggle/data/finale_test.csv", row.names = FALSE)
print("Done!")