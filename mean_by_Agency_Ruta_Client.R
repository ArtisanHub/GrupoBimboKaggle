library(data.table)

print("Reading data")
train <- fread('../input/train.csv', 
               select = c('Cliente_ID', 'Producto_ID', 'Agencia_ID', 'Ruta_SAK', 'Demanda_uni_equil'))

test <- fread('../input/test.csv', 
              select = c('id', 'Cliente_ID', 'Producto_ID', 'Agencia_ID', 'Ruta_SAK'))

print("Computing means")
#transform target variable to log(1 + demand) - this makes sense since we're 
#trying to minimize rmsle and the mean minimizes rmse:
train$log_demand = log1p(train$Demanda_uni_equil) 
mean_total <- mean(train$log_demand) #overall mean
#mean by product
mean_P <-  train[, .(MP = mean(log_demand)), by = .(Producto_ID)]
#mean by product and ruta
mean_PR <- train[, .(MPR = mean(log_demand)), by = .(Producto_ID, Ruta_SAK)] 
#mean by product, client, agencia
mean_PCA <- train[, .(MPCA = mean(log_demand)), by = .(Producto_ID, Cliente_ID, Agencia_ID)]

print("Merging means with test set")
submit <- merge(test, mean_PCA, all.x = TRUE, by = c("Producto_ID", "Cliente_ID", "Agencia_ID"))
submit <- merge(submit, mean_PR, all.x = TRUE, by = c("Producto_ID", "Ruta_SAK"))
submit <- merge(submit, mean_P, all.x = TRUE, by = "Producto_ID")

# Now create Predictions column;
submit$Pred <- expm1(submit$MPCA)*0.822+0.457
submit[is.na(Pred)]$Pred <- expm1(submit[is.na(Pred)]$MPR)*0.778+0.12
submit[is.na(Pred)]$Pred <- expm1(submit[is.na(Pred)]$MP)*1.045+0.6
submit[is.na(Pred)]$Pred <- expm1(mean_total) + 1.07

print("Write out submission file")
# now relabel columns ready for creating submission
setnames(submit,"Pred","Demanda_uni_equil")
# Any results you write to the current directory are saved as output.
write.csv(submit[,.(id,Demanda_uni_equil)],"submit_mean_by_Agency_Ruta_Client.csv", row.names = FALSE)
print("Done!")
