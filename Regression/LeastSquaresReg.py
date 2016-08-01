import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model


features = [] #featurs extracted from the training dataset
lables = []   #expected output taken as lables
test = []
temp = []
count = 0
val = 0

print("Getting data")

df_adv = pd.read_csv("D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/train.csv")

features = df_adv[['Agencia_ID', 'Canal_ID', 'Ruta_SAK', 'Cliente_ID', 'Producto_ID']]
lables = df_adv['Demanda_uni_equil']
print("Getting data complete")

# Create linear regression object
#regr = linear_model.LinearRegression(fit_intercept=True, normalize=True, copy_X=True, n_jobs=1)

# Create Basian Ridge object
#regr = linear_model.BayesianRidge()

regr = linear_model.RANSACRegressor(linear_model.LinearRegression())

print("fitting")
# Train the model using the training sets
regr.fit(features, lables)
print("fitting done")

# The coefficients
#print('Coefficients: \n', regr.coef_)

# The intercept
#print('Intercept: \n', regr.intercept_)

df_adv = pd.read_csv("D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/test.csv")

test = df_adv[['Agencia_ID', 'Canal_ID', 'Ruta_SAK', 'Cliente_ID', 'Producto_ID']]

output = open('D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/result.csv', 'w')

print("Predicting")

temp = abs(regr.predict(test))
#print()

print("Predicting done")
print("Output writing")

output.write("id,Demanda_uni_equil")
output.write(str("\n"))

#writing the output
for itm in temp:
    output.write(str(count))
    output.write(str(","))

    val = int(itm.item(0))
    output.write(str(val))

    output.write(str("\n"))
    count = count + 1

print("Finish")




