import numpy as np
from numpy.core.tests.test_mem_overlap import xrange


trainingData = open("/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/weeklySeperatedData/week3.csv","r")
w = 10
h = 1000
trainingDataArray = [[0 for x in range(w)] for y in range(h)]
trainingOutArray = [0 for x in range(h)]
count =0
tempArr = [10]
for line in trainingData:
 tempArr = line.split(",")
 trainingOutArray[count] = float(tempArr[10])
 column = 1;
 while(column<=9):
     trainingDataArray[count][column-1] = float(tempArr[column])
     column = column + 1
 count = count +1
 if count>=h:
     break

trainingDataArray = np.array(trainingDataArray)
trainingOutArray = np.array(trainingOutArray).T

syn0 = 2*np.random.random((w,h))
syn1 = 2*np.random.random((h,))

for j in xrange(100):
    l1 = 1/(1+np.exp(-(np.dot(trainingDataArray,syn0))))
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    l2_delta = (trainingOutArray - l2)*(l2*(1-l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
    syn1 += l1.T.dot(l2_delta)
    syn0 += trainingDataArray.T.dot(l1_delta)

print(trainingOutArray)
print(l2)

print(l2.shape)