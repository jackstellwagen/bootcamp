import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

#Set up defaults
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})


def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data)+1)/len(data)
    return(x, y)


xa_high = np.loadtxt('data/xa_high_food.csv', comments= '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments= '#')


fig, ax = plt.subplots(1, 1)
(x, y) = ecdf(xa_high)
_ = ax.plot(x, y, marker='.', linestyle='none')


(x, y) = ecdf(xa_low)

_ = ax.plot(x, y, marker='.', linestyle='none')


plt.show()
#
# xa_high_x = xa_high_n[0:-1,:1]
# xa_high_y = xa_high_n[0:-1,1:]
#
# xa_low_x = xa_low_n[0:-1,:1]
# xa_low_y = xa_low_n[0:-1,1:]
