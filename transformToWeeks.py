pathToTrainingSet = "/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/train.csv"
pathToConvertedFils = "/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/weeklySeperatedData"

trainingDataSet = open(pathToTrainingSet, "r")
week1 = open(pathToConvertedFils+'/week1.csv', 'w')
week2 = open(pathToConvertedFils+'/week2.csv', 'w')
week3 = open(pathToConvertedFils+'/week3.csv', 'w')
week4 = open(pathToConvertedFils+'/week4.csv', 'w')
week5 = open(pathToConvertedFils+'/week5.csv', 'w')
week6 = open(pathToConvertedFils+'/week6.csv', 'w')
week7 = open(pathToConvertedFils+'/week7.csv', 'w')
week8 = open(pathToConvertedFils+'/week8.csv', 'w')
week9 = open(pathToConvertedFils+'/week9.csv', 'w')

line =""

def week1Write():
    week1.write(line)

def week2Write():
    week2.write(line)

def week3Write():
    week3.write(line)

def week4Write():
    week4.write(line)

def week5Write():
    week5.write(line)

def week6Write():
    week6.write(line)

def week7Write():
    week7.write(line)

def week8Write():
    week8.write(line)

def week9Write():
    week9.write(line)


# map the inputs to the function blocks
options = {1: week1Write,
           3: week3Write,
           4: week4Write,
           5: week5Write,
           6: week6Write,
           7: week7Write,
           8: week8Write,
           9: week9Write,
}

for line in trainingDataSet:
    if not line.startswith("S"):
        options[int(line[0])]()

print("Training dataset has been successfully divided into 9 weeks")