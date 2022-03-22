import pandas as pd
import names
import random
import uuid
import datetime
topics=pd.read_csv('./data/topics.lst',sep='\t',header=None)
dummy_data=pd.DataFrame(columns=['id','name','dob','texts'])

def create_random_DoB():
    specific_dates=[1,15]
    range_of_years=[1980,2001]
    date=random.choice(specific_dates)
    year=random.choice(range(range_of_years[0],range_of_years[1]))
    month=random.choice(range(1,13))
    return f'''{date}/{month}/{year}'''

def create_random_conditions():
    conditions=open('./data/medical_conditions').readlines()
    return random.choice(conditions).replace('\n','')

for ii,texts in topics.itertuples():
    dummy_data.at[ii,'name']=names.get_full_name()
    dummy_data.at[ii,'texts']=texts
    dummy_data.at[ii,'dob']=create_random_DoB()
    #dummy_data.at[ii,'condition']=create_random_conditions()
    dummy_data.at[ii,'id']=str(uuid.uuid4())

dummy_data['dob']= pd.to_datetime(dummy_data['dob'],dayfirst=True)
dummy_data.to_csv('./data/dummy_patient_data.csv',sep='\t',index=False)