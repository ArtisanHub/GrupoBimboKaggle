pathToCompleteDataSet = "/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/train.csv"
pathToRquiredInputtDataSet = "/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/RelevantDataSet/requiredInput.csv"
pathToOutPutDataSet = "/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/RelevantDataSet/outPutData.csv"


completeDataSet = open(pathToCompleteDataSet,"r")
requiredDataSet = open(pathToRquiredInputtDataSet,"w")
outPutDataSet = open(pathToOutPutDataSet,"w")

for line in completeDataSet:
    if line.startswith("S"):
        continue
    row = line.split(",")
    requiredDataSet.write(row[2]+",")
    requiredDataSet.write(row[3]+",")
    requiredDataSet.write(row[4]+",")
    requiredDataSet.write(row[5]+"\n")
    outPutDataSet.write(row[10])
