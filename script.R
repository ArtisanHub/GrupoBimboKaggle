
library(data.table)

print("Reading data")
train <- fread('D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/train.csv', 
               select = c('Cliente_ID', 'Producto_ID', 'Agencia_ID', 'Ruta_SAK', 'Demanda_uni_equil'))

test <- fread('D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/test.csv', 
              select = c('id', 'Cliente_ID', 'Producto_ID', 'Agencia_ID', 'Ruta_SAK'))

print("Computing means")
#transform target variable to log(1 + demand) - this makes sense since we're 
#trying to minimize rmsle and the mean minimizes rmse:
train$log_demand = 1.0079999*log1p(train$Demanda_uni_equil+0.011599499)-0.0125995
mean_total <- median(train$log_demand) #overall mean

#mean by product
mean_P <-  train[, .(MP = median(log_demand)), by = .(Producto_ID)]
#mean by cliente
mean_C <-  train[, .(MC = median(log_demand)), by = .(Cliente_ID)]
#mean by product and agencia
mean_PA <- train[, .(MPA = median(log_demand)), by = .(Producto_ID, Agencia_ID)] 
#mean by product and ruta
mean_PR <- train[, .(MPR = median(log_demand)), by = .(Producto_ID, Ruta_SAK)] 
#mean by product, client, agencia
mean_PCA <- train[, .(MPCA = median(log_demand)), by = .(Producto_ID, Cliente_ID, Agencia_ID)]

print("Merging means with test set")
submit <- merge(test, mean_PCA, all.x = TRUE, by = c("Producto_ID", "Cliente_ID", "Agencia_ID"))
submit <- merge(submit, mean_PR, all.x = TRUE, by = c("Producto_ID", "Ruta_SAK"))
submit <- merge(submit, mean_PA, all.x = TRUE, by = c("Producto_ID", "Agencia_ID"))
submit <- merge(submit, mean_C, all.x = TRUE, by = "Cliente_ID")
submit <- merge(submit, mean_P, all.x = TRUE, by = "Producto_ID")

submit$Pred <- expm1(submit$MPCA)*0.7169+expm1(submit$MPR)*0.1823+0.1321
submit[is.na(Pred)]$Pred <- expm1(submit[is.na(Pred)]$MPR)*0.7399+0.19259
submit[is.na(Pred)]$Pred <- expm1(submit[is.na(Pred)]$MC)*0.822+0.8559
submit[is.na(Pred)]$Pred <- expm1(submit[is.na(Pred)]$MPA)*0.5249+0.95
submit[is.na(Pred)]$Pred <- expm1(submit[is.na(Pred)]$MP)*0.48+1
submit[is.na(Pred)]$Pred <- expm1(mean_total)-0.90

print("Write out submission file")
# now relabel columns ready for creatig submission
setnames(submit,"Pred","Demanda_uni_equil")
# Any results you write to the current directory are saved as output.
write.csv(submit[,.(id,Demanda_uni_equil)],"D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/result.csv", row.names = FALSE)
print("Done!")
