import numpy as np

#xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
#xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

def xa_to_diameter(xa):
    xa1 = xa * (4/np.pi)
    diameter = np.sqrt(xa1)
    return(diameter)
    #print(diameter)
