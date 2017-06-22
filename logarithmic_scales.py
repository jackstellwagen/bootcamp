import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns


data = np.loadtxt('data/collins_switch.csv', skiprows=2, delimiter=',')


#data[:, 1:]
iptg = data[:,:1]
gfp = data[:,1:2]
sem = data[:, 2:]

#identifying x,y
x = iptg
y = gfp

#labeling axis
fig, ax = plt.subplots(1, 1)
_ = ax.set_xlabel('IPTG')
_ = ax.set_ylabel('GFP')

#setting the x scale
ax.set_xscale('log')

ax.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.',
markersize=10)

#setting up the plot
_ = ax.plot(x, y, marker='.', linestyle='none')

plt.show()
