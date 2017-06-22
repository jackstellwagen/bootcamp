import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

#Set up defaults
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

#sns.set()

#load in data
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')

#Set up bin widths
bins = np.arange(1700, 2501, 50)

#Set up plot
fig, ax = plt.subplots(1, 1)
_ = ax.set_xlabel('cross section area (µm$^2$)')
_ = ax.set_ylabel('count')

#"Paint" the data
_ = ax.hist(xa_low, bins=bins)

plt.show()

#Save the figure
fig.savefig('practice_histogram.pdf')
