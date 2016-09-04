col0 = []
col1 = []
sep = ","

f = open( 'D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/bestmatchresult.csv', 'rU' ) #open train data
w = open('D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/newBestMatch.csv', 'w')

w.write("id,Demanda_uni_equil")
w.write(str("\n"))
for line in f:
    cells = line.split(",")
    print(cells)
    if cells[1] == "\n":

        w.write(str(cells[0]))
        w.write(sep)
        w.write(str(10))
        w.write(str("\n"))

    else:

        w.write(str(cells[0]))
        w.write(sep)
        w.write(str(cells[1]))

w.close()
f.close()