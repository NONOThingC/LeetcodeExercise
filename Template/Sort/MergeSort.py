amount=len(array)
interval=1
while interval<amount:
    for i in range(0,amount-interval,2*interval):
        # sort operation
        sort(array[i],array[i+interval])
return array