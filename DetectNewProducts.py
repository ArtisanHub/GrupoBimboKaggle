import pandas
import csv
import numpy as np
#####################
# Correlation
#####################
test = open("D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/test.csv", 'r', newline='')
train = open("D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/train.csv", 'r', newline='')
# array = []
# array = train.corr()["Demanda_uni_equil"]
#
# print(array)
array_test = []
array_train = []
dif_array = []
firstline = True
for line in test:
    if firstline:  # skip first line
        firstline = False
        continue
    line = line[:-1]
    row = line.split(",")
    array_test.append(row[6])
array_test = np.unique(array_test)
print(len(array_test))
firstline = True
for line in train:
    if firstline:  # skip first line
        firstline = False
        continue
    line = line[:-1]
    row = line.split(",")
    array_train.append(row[5])
array_train = np.unique(array_train)
print(len(array_train))
dif_array = np.setdiff1d(array_test,array_train)
print(len(dif_array))

output = open('D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/newProducts.csv', 'w')

#writing the output
for itm in dif_array:

    val = int(itm.item(0))
    output.write(str(val))
    output.write(str("\n"))

print("Finish")