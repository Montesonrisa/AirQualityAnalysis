import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pop = pd.read_csv('population.csv')
pop.drop(pop.columns[[0]], axis=1, inplace=True)
print(pop)
def bar ():
    loc = pop['LOCATION']
    pos = np.arange(len(loc))
    value = pop['2016']
    plt.figure()
    bars = plt.bar(pos, value, align='center')
    plt.title('Populacja w 2016', fontsize=9)
    plt.xlabel('Lokalizacja', fontsize=9)
    plt.ylabel('Wielkość populacji', fontsize=9)
    plt.legend(['2016'], fontsize=9)
    plt.xticks(pop.index, pop['LOCATION'], rotation='vertical', fontsize=9)
    plt.subplots_adjust(top=0.8, bottom=0.3, left=0.2, right=0.9)
    for bar in bars:
        plt.gca().text(bar.get_x() + bar.get_width()/2, bar.get_height(), str(int(bar.get_height())), ha='center', color='black', fontsize=8)
    return plt.show()