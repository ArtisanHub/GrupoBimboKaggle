pathToCompleteDataSet = "/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/weeklySeperatedData/week4.csv"
pathToRquiredInputtDataSet = "/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/weeklySeperatedData/week4Relevant.csv"



completeDataSet = open(pathToCompleteDataSet,"r")
requiredDataSet = open(pathToRquiredInputtDataSet,"w")


# Input and output in seperate files
# pathToOutPutDataSet = "/home/rnavagamuwa/Documents/CSE/Semester7/DataMining/kaggle/weeklySeperatedData/outPutData.csv"
# outPutDataSet = open(pathToOutPutDataSet,"w")
# for line in completeDataSet:
#     if line.startswith("S"):
#         continue
#     row = line.split(",")
#     requiredDataSet.write(row[2]+",")
#     requiredDataSet.write(row[3]+",")
#     requiredDataSet.write(row[4]+",")
#     requiredDataSet.write(row[5]+"\n")
#     outPutDataSet.write(row[10])
#


# input and output in the same file
for line in completeDataSet:
    if line.startswith("S"):
        continue
    row = line.split(",")
    requiredDataSet.write(row[2]+",")
    requiredDataSet.write(row[3]+",")
    requiredDataSet.write(row[4]+",")
    requiredDataSet.write(row[5]+",")
    requiredDataSet.write(row[10])