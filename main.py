import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web

style.use('ggplot')

START = dt.datetime(2015, 1, 1)
END = dt.datetime.now()

df = web.DataReader("AAPL", 'yahoo', START, END)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

df.to_csv('AAPL.csv')

print(df.head())