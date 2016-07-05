from sklearn import tree
import csv

features = [] #featurs extracted from the training dataset
lables = []   #expected output taken as lables
test = []
temp = []
count = 0
val = 0

f = open( 'D:/FYP/DM/DecisionTreeBimbo/Data/data.csv', 'rU' ) #open train data
for line in f:
    cells = line.split( "," )
    features.append( ( cells[ 0 ], cells[ 1 ], cells[ 3 ], cells[ 4 ] ) )
    lables.append((cells[5], cells[6], cells[7], cells[8], cells[9]))
f.close()


#putting up the decision tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, lables)

f = open( 'D:/FYP/DM/DecisionTreeBimbo/Data/test.csv', 'rU' ) #open test data
for line in f:
    cells = line.split( "," )
    test.append( ( cells[ 1 ], cells[ 2 ], cells[ 4 ], cells[ 5 ] ) )

f.close()

output = open('D:/FYP/DM/DecisionTreeBimbo/Data/result.csv', 'w')

for itm in test:
    temp.append(clf.predict(itm))


output.write("id,Demanda_uni_equil")
output.write(str("\n"))

#writing the output
for itm in temp:
    output.write(str(count))
    output.write(str(","))

    val = int(itm.item(4))
    output.write(str(val))

    output.write(str("\n"))
    count = count + 1


