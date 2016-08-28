import  csv
import BestMatchingNumber as bm
# from __builtin__ import dict

pathToTrainingSet = "/home/jawadhsr/Desktop/Kaggle/input/weeks/"
maps = dict()
with open(pathToTrainingSet+"week3.csv",'rb') as csvfile :
    reader = csv.reader(csvfile)
    for row in reader:
        var =  row[2]+','+row[3]+','+row[4]+','+row[5]
        if(maps.has_key(var)):
            # maps.update(var,append(row[10])
            maps.get(var).append(row[10])
        else:
            maps.setdefault(var,[row[10]])

result_map = dict()
for key in maps:
    result_map.setdefault(key,bm.bestMatch(maps[key],3))

# Here I have made the corresponding rows as a comma seperated string and



