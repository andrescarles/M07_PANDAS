import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('test.csv')
def funcion1():
    return df['battery_power'].head(10)

def funcion2():
    return df[['px_width','px_height']].head(10)

def funcion3():
    return df['clock_speed'].head(10)

def funcion4():
    funcion1().plot.bar(legend=True)
    plt.show()
    funcion2().plot.bar(legend=True)
    plt.show()
    funcion3().plot.bar(legend=True)
    plt.show()
