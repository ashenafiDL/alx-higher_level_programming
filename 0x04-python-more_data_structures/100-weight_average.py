#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    sums, weight = 0, 0
    if len(my_list) > 0:
        for i in my_list:
            sums += i[0] * i[1]
            weight += i[1]
        average = sums / weight
    return average
