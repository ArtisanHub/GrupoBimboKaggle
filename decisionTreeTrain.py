from sklearn import tree

features = []
lables = []
test = []

f = open( 'D:/FYP/DM/DecisionTreeBimbo/Data/data.csv', 'rU' ) #open the file in read universal mode
for line in f:
    cells = line.split( "," )
    features.append( ( cells[ 0 ], cells[ 1 ], cells[ 2 ], cells[ 3 ], cells[ 4 ], cells[ 5 ] ) ) #since we want the first, second and third column
    lables.append((cells[6], cells[7], cells[8], cells[9], cells[10],))
f.close()



clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, lables)

f = open( 'D:/FYP/DM/DecisionTreeBimbo/Data/test.csv', 'rU' ) #open the file in read universal mode
for line in f:
    cells = line.split( "," )
    test.append( ( cells[ 0 ], cells[ 1 ], cells[ 2 ], cells[ 3 ], cells[ 4 ], cells[ 5 ] ) ) #since we want the first, second and third column

f.close()

output = open('D:/FYP/DM/DecisionTreeBimbo/Data/result.csv', 'w')

for itm in test:
    output.write(str(clf.predict(itm)))
    print(clf.predict(itm))



