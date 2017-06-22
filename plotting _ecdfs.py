def ecdf(data):
    x = np.sort(date)
    y = np.arange(1, len(data)+1)/len(data)
    return(x,y)

xa_high = open('data/xa_high_food.csv')
xa_low = open('data/xa_low_food.csv')

xa_high_n = ecdf(xa_high)
xa_low_n = ecdf(xa_low)
