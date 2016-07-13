from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)


filepathSalih = '/home/jawadhsr/Desktop/Kaggle/trani.csv'
filepathRandika = '/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/weeklySeperatedData/week3.csv'

# load pima indians dataset
dataset = numpy.loadtxt(filepathRandika, delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:10]
Y = dataset[:,10]
# create model
model = Sequential()
model.add(Dense(12, input_dim=10, init='uniform', activation='relu'))

# given that activation function as 'softplus' as it's range is (0,inf)
model.add(Dense(8, init='uniform', activation='softplus'))
model.add(Dense(1, init='uniform', activation='softplus'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, nb_epoch=150, batch_size=10)
# evaluate the model
scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# Above you could use testing data so that w can check the accuracy with that data. :)
