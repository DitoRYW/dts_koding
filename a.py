# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:24:10 2019

@author: Mulmed
"""

from sqlalchemy import create_engine
import pandas as pd
from pandas.io import sql
#import numpy as np
data = pd.read_excel('H:\\avsf\personalia.xls')
#engine = create_engine('sqlite:///:memory;')
#data.to.sql('data_table', engine)
#res1=pd.read_sql_query('SELECT * FROM data_table', engine)
print(res1)
#print(data)
#print(data['Gender'])
#print (data.loc[:,['Pendidikan','Gender','Gaji']])
#print ("")
#print (data.loc[:,['Gender','Usia']])



#with pd.ExcelFile('H:\\avsf\\ww\\b.xlsx') as xlsx:
    #df1 = pd.read_excel(xlsx, 'Sheet1')
    #df2 = pd.read_excel(xlsx, 'Sheet2')
    
#print("Hasil Sheet 1")
#print (df1[0:5]['salary'])
#print ("")
#print("Hasil Sheet 2")
#print (df2[0:5]['zipcode'])
    
