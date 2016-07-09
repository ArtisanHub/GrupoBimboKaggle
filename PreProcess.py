import pandas


#####################
# Correlation
#####################

train = pandas.read_csv("/home/prashan/Desktop/DM/Kaggle/data/train.csv")
array = []
array = train.corr()["Demanda_uni_equil"]
print(array)


#####################
#Mean Value
#####################

