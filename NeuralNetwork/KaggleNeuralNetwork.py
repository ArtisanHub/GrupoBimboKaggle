from keras.models import Sequential
from keras.layers import Dense

pathToInputDataSet = "/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/weeklySeperatedData/train.csv"
inputDataSet = open(pathToInputDataSet,"r")


inputDataArr = []
outputDataArray = []

for line in inputDataSet:
     row =[ int(n) for n in line.replace("\n","").split(",")]
     outputDataArray.append(row[4])
     row.pop()
     inputDataArr.append(row)

X = inputDataArr
Y = outputDataArray

print("Data-set has been successfully loaded into two arrays")

# create model
model = Sequential()
model.add(Dense(12, input_dim=4, init='uniform', activation='linear'))
model.add(Dense(8, init='uniform', activation='linear'))
model.add(Dense(1, init='uniform', activation='linear'))
# Compile model
model.compile(loss='mae', optimizer='Adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, nb_epoch=150, batch_size=10)


pathToTestDataSet = "/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/weeklySeperatedData/week7.csv"
inputTestDataSet = open(pathToInputDataSet,"r")

inputDataArr = []
outputDataArray = []

for line in inputTestDataSet:
     row =[ int(n) for n in line.replace("\n","").split(",")]
     outputDataArray.append(row[4])
     row.pop()
     inputDataArr.append(row)

X = inputDataArr
Y = outputDataArray

# evaluate the model
scores = model.evaluate(X, Y)
# out = model.predict(X)
# for l in out:
#     print(str(round(float(l)))+"\n")
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
