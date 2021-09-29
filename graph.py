import numpy as np
import pandas as pd
from datetime import date, datetime
import locale
locale.setlocale(locale.LC_ALL, 'en_IN')

def datafilter():
    # change the directory , copy the file into appr. folder b4 deploying in heroku
    file = r'csv_files\india_brazil_cases.csv'
    df = pd.read_csv(file)
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    if(d1 < '2021-10-11'):
           df = df[df['Date'] >= d1][:5]
    else:
        df = df.tail()
    df['Date'] = df['Date'].apply(lambda x:datetime.strptime(x, '%Y-%m-%d').strftime('%d %B,%Y'))
    df['Cases in India'] = df['Cases in India'].apply(lambda x:f'{x:n}')
    df['Cases in Brazil'] = df['Cases in Brazil'].apply(lambda x:f'{x:n}')
    df.reset_index(drop = True, inplace = True)
    if(d1 <= '2021-10-15'):
        d1 = datetime.strptime(d1, '%Y-%m-%d').strftime('%d %B,%Y')
        df.loc[(df['Date'] == d1),'Date'] = d1 +'  (today)'

    return df

def filter():
    # change the directory , copy the file into appr. folder b4 deploying in heroku
    file = r'csv_files\LR_SVM.csv'
    df_new = pd.read_csv(file)
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    if(d1 < '2021-10-11'):
           df_new = df_new[df_new['Date'] >= d1][:5]
    else:
        df_new = df_new.tail()
    df_new['Date'] = df_new['Date'].apply(lambda x:datetime.strptime(x, '%Y-%m-%d').strftime('%d %B,%Y'))
    for i in ['Brazil svm','Brazil LR','India svm','India LR']:
        df_new[i] = df_new[i].apply(lambda x:f'{x:n}')
    df_new.reset_index(drop = True, inplace = True)
    if(d1 <= '2021-10-15'):
        d1 = datetime.strptime(d1, '%Y-%m-%d').strftime('%d %B,%Y')
        df_new.loc[(df_new['Date'] == d1), 'Date'] = d1 +'  (Today)'

    return df_new
