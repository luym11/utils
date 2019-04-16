import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('result')
data = df.iloc[:,1]

def get_number(str):
    li = [s for s in str.split(':')]
    return float(li[1])

data1 = data.apply(get_number)
data1.plot()
plt.show()
