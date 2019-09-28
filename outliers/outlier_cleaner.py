#!/usr/bin/python
import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """



    cleaned_data = []
    ### your code goes here


    #predictions, ages, net_worths
    #(age, net_worth, error)

    for i in range(len(predictions)):

        error = predictions[i] - net_worths[i]
        error = abs(error)

        lst = []
        lst.extend([ ages[i] , net_worths[i] , error ])
        lst = tuple(lst)

        cleaned_data.append(lst)

    cleaned_data.sort(key= lambda tup : tup[2])

    remn =  int( 0.9 * len(ages))

    cleaned_data = cleaned_data[:remn]

    return cleaned_data

