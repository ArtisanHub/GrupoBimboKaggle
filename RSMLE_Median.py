import numpy as np
import pandas as pd
import time
from collections import defaultdict
from sklearn.base import BaseEstimator
from random import random
from random import randint


########################################
# Median Class
########################################

class Median(BaseEstimator):
    def __init__(self, keys):
        self.keys = keys
        self.total = 0
        self.not_found = 0

    def fit(self, X, y=None):
        start_time = time.time()
        block = pd.concat([X, y], axis=1)  # concatination of both x and y blocks into one block
        target = block.columns[-1]  # Demanda_uni_equil is our target
        # all keys dict
        all_keys = block.groupby(self.keys)['Demanda_uni_equil'].apply(lambda x: self.getval(x))
        # all_keys = block.groupby(self.keys).agg({target: np.median})

        # initalise dict list
        self.dicts = [all_keys.to_dict()]  # here map has been creaated for given keys (A,B,C -> demand)
        print("Complete first part in --- %s seconds -----" % (time.time() - start_time))

        start_time = time.time()
        for n in range(1, len(self.keys)):
            keys = self.keys[:-n]
            key_grouped = block.groupby(keys).agg({target: np.median})
            self.dicts.append(key_grouped.to_dict()[target])
            print("finish x")
        print("Complete Fit last part in --- %s seconds -----" % (time.time() - start_time))
        global_median = np.median(y)
        self.dicts.append(defaultdict(lambda: global_median))
        return self

    # get mapped trained value for test data
    def fetch_value_from_trained_dic(self, keys, dicts):
        tkey = tuple(keys)
        # if tkey in dicts[0].keys():
        try:
            return dicts[0][tkey]
        # else:
        except KeyError:
            return self.fetch_value_from_trained_dic(keys[:-1], dicts[1:])

    def predict(self, X):
        return X[self.keys].apply(lambda t: self.fetch_value_from_trained_dic(t, self.dicts),
                                  axis=1)  # get key columns and check with train data

    def getval(self, keys):
        array = tuple(keys)

        array = np.unique(array)
        array_length = len(array)
        rsmleValues_array = []
        count = 0
        maxValue = np.amax(array)
        minValue = np.amin(array)



        for i in array:
            count = 0
            for j in array:
                count = count + (np.log1p(i) - np.log1p(j))**2
            rsmleValues_array.append(np.sqrt(count / array_length))

        count = -1;
        index = 0
        min_error_value = rsmleValues_array[0]
        for val in rsmleValues_array:
            count += 1
            if val < min_error_value:
                min_error_value = val
                index = count

        demand = array[index]
        return demand

        # for i in range(minValue, maxValue+1):
        #     count = 0
        #     for j in array:
        #         count = count + (np.log1p(i) - np.log1p(j))**2
        #     rsmleValues_array.append(np.sqrt(count / array_length))
        #
        # count = -1;
        # index = 0
        # min_error_value = rsmleValues_array[0]
        # for val in rsmleValues_array:
        #     count += 1
        #     if val < min_error_value:
        #         min_error_value = val
        #         index = count
        #
        # demand = index + minValue
        # return demand


######################################
# rejection Sampling class
######################################

class RejectionSampling(object):
    def __init__(self, iterator, k=1):
        self.iterator = iterator
        self.k = k
        self.ans = []

    def run(self):
        n = 0.0
        for x in self.iterator:
            n += 1.0
            r = random()  # returns numbers between 0 and 1
            if r < (self.k / n):
                self.__accept(x, n)
        return self.ans

    def __accept(self, x, n):
        if len(self.ans) == self.k:
            idx = randint(0, self.k - 1)
            del self.ans[idx]
        self.ans.append(x)


def get_data(N, quick=False):
    chunk = 10 ** 4  # 10^3 = 1000
    columns = ['Semana', 'Agencia_ID', 'Canal_ID', 'Ruta_SAK', 'Cliente_ID', 'Producto_ID', 'Demanda_uni_equil']

    if quick:
        df_train = pd.read_csv('D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/train.csv', usecols=columns, nrows=40000)
    else:
        data = pd.read_csv('D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/train.csv', usecols=columns)
        # chunks = RejectionSampling(data, N).run()
        # df_train = pd.concat(chunks, ignore_index=True)

    X = data[['Semana', 'Agencia_ID', 'Canal_ID', 'Ruta_SAK', 'Cliente_ID', 'Producto_ID']]  # .values
    y = data['Demanda_uni_equil']
    return [X, y]


def submit(estimator, cols):
    # cols = ['Agencia_ID','Canal_ID','Ruta_SAK','Cliente_ID','Producto_ID']
    df_test = pd.read_csv('D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/test.csv')
    sub = pd.read_csv('D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/sample_submission.csv')
    sub['Demanda_uni_equil'] = estimator.predict(df_test)
    print("Writing file")
    sub.to_csv('D:/FYP-Developments/Dataset-Kaggale/MedianRejectionSamplingData/result.csv', index=False)


if __name__ == "__main__":
    start_time = time.time()
    N = 8000
    # [X,y] = get_data(N, quick=True)


    print("Getting data")
    [X, y] = get_data(N)
    print("Complete getting data in --- %s seconds -----"  % (time.time() - start_time))


    # print(X.shape)  # this comes from pandas - prints no of rows and cols

    keys = ['Canal_ID', 'Ruta_SAK', 'Producto_ID', 'Cliente_ID']

    clf = Median(keys)
    print("Running Fit")
    clf.fit(X, y)
    print("Predicting")
    start_time = time.time()
    submit(clf, keys)
    print("Complete predictinga in --- %s seconds -----" % (time.time() - start_time))

    print("Done")
