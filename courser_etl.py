import glob
import pandas as pd

def extract():
    all_data=[]
    for csvfile in glob.glob('*.csv'):
        all_data.append(pd.read_csv(csvfile))

    for jsonfile in glob.glob('*.json'):
        all_data.append(pd.read_json(jsonfile))

    extracted_data=pd.concat(all_data,ignore_index=True)

    return extracted_data

def transform(data):
    data=data.drop_duplicates()
    data=data.dropna()
    data['name']=data['name'].str.title()
    data=data.sort_values(by='name',ascending=True,ignore_index=True)
    return data

def load(data):
    data.to_csv('czystepliki.csv', index=False)
    print('sukces!')


load(transform(extract()))