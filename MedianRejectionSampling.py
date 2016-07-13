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
        block = pd.concat([X, y], axis=1)  # concatination of both x and y blocks into one block
        target = block.columns[-1]  # Demanda_uni_equil is our target
        # all keys dict
        all_keys = block.groupby(self.keys).agg({target: np.median})

        # initalise dict list
        self.dicts = [all_keys.to_dict()[target]]  # here map has been creaated for given keys (A,B,C -> demand)

        # all other dicts ( There can be other combinations as well,like A,B, A)
        for n in range(1, len(self.keys)):
            keys = self.keys[:-n]
            key_grouped = block.groupby(keys).agg({target: np.median})
            self.dicts.append(key_grouped.to_dict()[target])

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
        df_train = pd.read_csv('/home/prashan/Desktop/DM/Kaggle/data/train.csv', usecols=columns, nrows=40000)
    else:
        data = pd.read_csv('/home/prashan/Desktop/DM/Kaggle/data/train.csv', usecols=columns, iterator=True,
                           chunksize=chunk)
        chunks = RejectionSampling(data, N).run()
        df_train = pd.concat(chunks, ignore_index=True)

    X = df_train[['Semana', 'Agencia_ID', 'Canal_ID', 'Ruta_SAK', 'Cliente_ID', 'Producto_ID']]  # .values
    y = df_train['Demanda_uni_equil']
    return [X, y]


def submit(estimator, cols):
    # cols = ['Agencia_ID','Canal_ID','Ruta_SAK','Cliente_ID','Producto_ID']
    df_test = pd.read_csv('/home/prashan/Desktop/DM/Kaggle/data/test.csv')
    sub = pd.read_csv('/home/prashan/Desktop/DM/Kaggle/data/sample_submission.csv')
    sub['Demanda_uni_equil'] = estimator.predict(df_test)
    sub.to_csv('/home/prashan/Desktop/DM/Kaggle/data/result2.csv', index=False)


if __name__ == "__main__":
    N = 8000
    # [X,y] = get_data(N, quick=True)
    [X, y] = get_data(N)
    # print(X.shape)  # this comes from pandas - prints no of rows and cols

    keys = ['Canal_ID', 'Ruta_SAK', 'Producto_ID', 'Cliente_ID']

    clf = Median(keys)
    clf.fit(X, y)
    submit(clf, keys)
