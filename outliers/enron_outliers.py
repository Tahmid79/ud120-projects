#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary , bonus)

matplotlib.pyplot.xlabel("Salary")
matplotlib.pyplot.ylabel("Bonus")

matplotlib.pyplot.show()

mn_lst = []

for name , information in data_dict.items():

    if(information['salary'] != 'NaN' and information['bonus'] != 'NaN'  ):

         lst = []
         lst.extend([name , information['salary'] , information['bonus']  ] )
         lst = tuple(lst)
         mn_lst.append(lst)

mn_lst = sorted(mn_lst , key = lambda x : (x[1],x[2] ) , reverse=True)

print (mn_lst)



