#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:S

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))


slry_ct = 0
eml_ct = 0

for person , information in enron_data.items() :
    if information['salary'] == 'NaN' :
        slry_ct+=1
    if information['email_address'] =='NaN' :
        eml_ct +=1



print ('Salary = ' + str(slry_ct) )
print ('Email = ' + str(eml_ct) )
