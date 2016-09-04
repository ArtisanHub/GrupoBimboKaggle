import pandas as pd
import csv
import numpy as np


######################################################
# Correlation
######################################################

train = pd.read_csv("D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/train.csv")

array = []
array = train.corr()["Demanda_uni_equil"]

print(array)


######################################################
# New Product extraction
######################################################


# test = open("/home/prashan/Desktop/DM/Kaggle/data/test.csv", 'r', newline='')
# train = open("/home/prashan/Desktop/DM/Kaggle/data/train.csv", 'r', newline='')
#
# array_test = []
# array_train = []
# dif_array = []
#
#
# firstline = True
#
# for line in test:
#     if firstline:  # skip first line
#         firstline = False
#         continue
#     line = line[:-1]
#     row = line.split(",")
#     array_test.append(row[6])
#
# array_test = np.unique(array_test)
# print(len(array_test))
#
# firstline = True
#
# for line in train:
#     if firstline:  # skip first line
#         firstline = False
#         continue
#     line = line[:-1]
#     row = line.split(",")
#     array_train.append(row[5])
#
# array_train = np.unique(array_train)
# print(len(array_train))
#
# dif_array = np.setdiff1d(array_test, array_train)
#
# print(len(dif_array))
#
# np.savetxt("/home/prashan/Desktop/DM/Kaggle/data/New_Products_From_Test_File.csv", dif_array, delimiter=",")


