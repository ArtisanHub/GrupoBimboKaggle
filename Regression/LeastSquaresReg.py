from sklearn import linear_model


features = [] #featurs extracted from the training dataset
lables = []   #expected output taken as lables
test = []
temp = []
count = 0
val = 0

print("Getting data")

f = open( 'D:/FYP-Developments/Dataset-Kaggale/weeklySeperatedData/week3.csv', 'rU' ) #open train data
for line in f:
    cells = line.split(",")
    features.append((float(cells[ 2 ]), float(cells[ 3 ]), float(cells[ 4 ]), float(cells[ 5 ])))
    lables.append(float(cells[10]))
f.close()
print("week3 done")

f = open( 'D:/FYP-Developments/Dataset-Kaggale/weeklySeperatedData/week4.csv', 'rU' ) #open train data
for line in f:
    cells = line.split(",")
    features.append((float(cells[ 2 ]), float(cells[ 3 ]), float(cells[ 4 ]), float(cells[ 5 ])))
    lables.append(float(cells[10]))
f.close()
print("week4 done")

f = open( 'D:/FYP-Developments/Dataset-Kaggale/weeklySeperatedData/week5.csv', 'rU' ) #open train data
for line in f:
    cells = line.split(",")
    features.append((float(cells[ 2 ]), float(cells[ 3 ]), float(cells[ 4 ]), float(cells[ 5 ])))
    lables.append(float(cells[10]))
f.close()
print("week5 done")

f = open( 'D:/FYP-Developments/Dataset-Kaggale/weeklySeperatedData/week6.csv', 'rU' ) #open train data
for line in f:
    cells = line.split(",")
    features.append((float(cells[ 2 ]), float(cells[ 3 ]), float(cells[ 4 ]), float(cells[ 5 ])))
    lables.append(float(cells[10]))
f.close()
print("week6 done")

f = open( 'D:/FYP-Developments/Dataset-Kaggale/weeklySeperatedData/week7.csv', 'rU' ) #open train data
for line in f:
    cells = line.split(",")
    features.append((float(cells[ 2 ]), float(cells[ 3 ]), float(cells[ 4 ]), float(cells[ 5 ])))
    lables.append(float(cells[10]))
f.close()
print("week7 done")

f = open( 'D:/FYP-Developments/Dataset-Kaggale/weeklySeperatedData/week8.csv', 'rU' ) #open train data
for line in f:
    cells = line.split(",")
    features.append((float(cells[ 2 ]), float(cells[ 3 ]), float(cells[ 4 ]), float(cells[ 5 ])))
    lables.append(float(cells[10]))
f.close()
print("week8 done")

f = open( 'D:/FYP-Developments/Dataset-Kaggale/weeklySeperatedData/week9.csv', 'rU' ) #open train data
for line in f:
    cells = line.split(",")
    features.append((float(cells[ 2 ]), float(cells[ 3 ]), float(cells[ 4 ]), float(cells[ 5 ])))
    lables.append(float(cells[10]))
f.close()
print("week9 done")


# Create linear regression object
#regr = linear_model.LinearRegression()

# Create Basian Ridge object
regr = linear_model.BayesianRidge()

print("fitting")
# Train the model using the training sets
regr.fit(features, lables)
print("fitting done")

f = open( 'D:/FYP-Developments/Dataset-Kaggale/test.csv', 'rU' ) #open test data
for line in f:
    cells = line.split( "," )
    test.append((float(cells[ 2 ]), float(cells[ 3 ]), float(cells[ 4 ]), float(cells[ 5 ])))

f.close()

output = open('D:/FYP-Developments/Dataset-Kaggale/resultBasianRidge.csv', 'w')

print("Predicting")
for itm in test:

    temp.append(abs(regr.predict(itm)))

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

