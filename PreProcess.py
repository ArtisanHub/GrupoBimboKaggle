import pandas


#####################
# Correlation
#####################

train = pandas.read_csv("D:/FYP-Developments/DebsDataset/KaggaleDataset/train.csv")

array = []
array = train.corr()["Demanda_uni_equil"]

print(array)


#####################
#Mean Value
#####################

