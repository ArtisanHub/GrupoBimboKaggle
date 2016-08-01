import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

x_train = [] #featurs extracted from the training dataset
y_train = []   #expected output taken as lables
x_test = []
y_test = []
degree = 3
count = 0
val = 0

print("Getting data")

df_adv = pd.read_csv("D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/train.csv")

x_train = df_adv[['Canal_ID', 'Ruta_SAK', 'Cliente_ID', 'Producto_ID']]
y_train = df_adv['Demanda_uni_equil']
print("Getting data complete")


print("fitting")
model = make_pipeline(PolynomialFeatures(degree), Ridge())
model.fit(x_train, y_train)
print("fitting done")


df_adv = pd.read_csv("D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/test.csv")

x_test = df_adv[['Canal_ID', 'Ruta_SAK', 'Cliente_ID', 'Producto_ID']]
y_test = model.predict(x_test)

print("Predicting done")
print("Output writing")

output = open('D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/result.csv', 'w')

output.write("id,Demanda_uni_equil")
output.write(str("\n"))

#writing the output
for itm in y_train:

    output.write(str(count))
    output.write(str(","))

    val = int(itm.item(0))
    output.write(str(val))

    output.write(str("\n"))
    count = count + 1

print("Finish")

