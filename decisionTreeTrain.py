from sklearn import tree
import csv

features = [] #featurs extracted from the training dataset
lables = []   #expected output taken as lables
test = []
temp = []
count = 0
val = 0

f = open( 'D:/FYP-Developments/DebsDataset/KaggaleDataset/weeklySeperatedData/week3.csv', 'rU' ) #open train data
for line in f:
    cells = line.split( "," )
    features.append( ( cells[ 2 ], cells[ 3 ], cells[ 5 ] ) )
    lables.append((cells[10]))
f.close()

f = open( 'D:/FYP-Developments/DebsDataset/KaggaleDataset/weeklySeperatedData/week4.csv', 'rU' ) #open train data
for line in f:
    cells = line.split( "," )
    features.append( ( cells[ 2 ], cells[ 3 ], cells[ 5 ] ) )
    lables.append((cells[10]))
f.close()

f = open( 'D:/FYP-Developments/DebsDataset/KaggaleDataset/weeklySeperatedData/week5.csv', 'rU' ) #open train data
for line in f:
    cells = line.split( "," )
    features.append( ( cells[ 2 ], cells[ 3 ], cells[ 5 ] ) )
    lables.append((cells[10]))
f.close()

f = open( 'D:/FYP-Developments/DebsDataset/KaggaleDataset/weeklySeperatedData/week6.csv', 'rU' ) #open train data
for line in f:
    cells = line.split( "," )
    features.append( ( cells[ 2 ], cells[ 3 ], cells[ 5 ] ) )
    lables.append((cells[10]))
f.close()

f = open( 'D:/FYP-Developments/DebsDataset/KaggaleDataset/weeklySeperatedData/week7.csv', 'rU' ) #open train data
for line in f:
    cells = line.split( "," )
    features.append( ( cells[ 2 ], cells[ 3 ], cells[ 5 ] ) )
    lables.append((cells[10]))
f.close()

f = open( 'D:/FYP-Developments/DebsDataset/KaggaleDataset/weeklySeperatedData/week8.csv', 'rU' ) #open train data
for line in f:
    cells = line.split( "," )
    features.append( ( cells[ 2 ], cells[ 3 ], cells[ 5 ] ) )
    lables.append((cells[10]))
f.close()

f = open( 'D:/FYP-Developments/DebsDataset/KaggaleDataset/weeklySeperatedData/week9.csv', 'rU' ) #open train data
for line in f:
    cells = line.split( "," )
    features.append( ( cells[ 2 ], cells[ 3 ], cells[ 5 ] ) )
    lables.append((cells[10]))
f.close()


#putting up the decision tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, lables)


f = open( 'D:/FYP-Developments/DebsDataset/KaggaleDataset/test.csv', 'rU' ) #open test data
for line in f:
    cells = line.split( "," )
    test.append(( cells[ 3 ], cells[ 4 ], cells[ 6 ] ))

f.close()

output = open('D:/FYP-Developments/DebsDataset/KaggaleDataset/result.csv', 'w')

for itm in test:
    temp.append(clf.predict(itm))


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

