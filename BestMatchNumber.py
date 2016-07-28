import numpy as np
import random as rnd

data = list()
for r in xrange(10000):
    data.append(rnd.randint(5,70))
    r = r+1

#  You can just use below function to calculate the impacting data set mean.
#  Just copy this function and paste it in a relevent location.which do a significant impact to the data set
#  usually 'stdCoefficient' is 1 as it gives 65% of data
#  an Example function call : bestMatch(data,1) 
def bestMatch(arr,stdCoefficient) :

    std = np.std(arr)
    mean = np.mean(arr)
    # print(arr)
    lRange = np.abs(stdCoefficient*std-mean)
    rRange = np.abs(stdCoefficient*std+mean)
    # print(std)
    # print(np.mean(arr))
    # print(lRange)
    # print(rRange)
    # print (len(arr))
    i=0
    newlist = list()
    while (i< len(arr)):
        if arr[i] >= lRange and arr[i] <= rRange:
            newlist.append(arr[i])
        i = i+1
    # print (len(newlist))
    # print ('New Mean', np.mean(newlist))
    # plt.plot(norm.pdf(newlist,mean,std),arr)
    # plt.hist(arr,normed=True)
    # plt.plot(pdfarr)
    # plt.ylabel('Numbers')
    # plt.show()


    return np.mean(newlist) # This would either be mean,median or mode.



bestMatch(data)
