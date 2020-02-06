# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:01:07 2020

@author: richard
"""

import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header = None)

df.head(10)
df.tail(10)

headers=["symboling","normalized-losses","make"]
df.columns = headers

# set path to export
path="c:\\data\\automobile.csv"
# export dataframe
df.to_csv(path)
jsonpath="c:\\data\\automobile.json"
df.to_json(jsonpath)

df.dtypes
df.describe()
df.describe(include="all")
df.info()


