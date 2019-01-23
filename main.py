import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader as web

style.use('ggplot')

START = dt.datetime(2015, 1, 1)
END = dt.datetime.now()

df = web.DataReader("TSLA", 'morningstar', START, END)

print(df.head())