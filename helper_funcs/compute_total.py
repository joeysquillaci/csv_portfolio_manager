def compute_total(entry):

    num = 0

    for i in range(1, len(entry)):
    
        balance_flt = float(entry[i])
        num = balance_flt + num

    return "{:.2f}".format(num)

