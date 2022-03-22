import pandas as pd
import names
import random
import uuid

topics=pd.read_csv('topics.lst',sep='\t',header=None)
dummy_data=pd.DataFrame(columns=['ID','Name','DoB','Condition','Texts'])

def create_random_DoB():
    specific_dates=[1,15]
    range_of_years=[1980,2001]
    date=random.choice(specific_dates)
    year=random.choice(range(range_of_years[0],range_of_years[1]))
    month=random.choice(range(1,13))
    return f'''{date}/{month}/{year}'''

def create_random_conditions():
    conditions=open('medical_conditions').readlines()
    return random.choice(conditions).replace('\n','')

for ii,texts in topics.itertuples():
    dummy_data.at[ii,'Name']=names.get_full_name()
    dummy_data.at[ii,'Texts']=texts
    dummy_data.at[ii,'DoB']=create_random_DoB()
    dummy_data.at[ii,'Condition']=create_random_conditions()
    dummy_data.at[ii,'ID']=str(uuid.uuid4())

dummy_data.to_csv('dummy_patient_data.csv',sep='\t',index=False)