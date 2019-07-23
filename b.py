# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:44:19 2019

@author: Mulmed
"""

from sqlalchemy import create_engine
from pandas.io import sql

import pandas as pd

data = pd.read_csv('H:\\avsf\personalia.csv')

engine = create_engine('sqlite:///:memory:')

data.to_sql('data_table', engine)

#==================================================
#res1=pd.read_sql_query('SELECT * FROM data_table', engine)

#print('Result 1')
#nomor 1 ==============================================
#print(res1)

res2 = pd.read_sql_query('SELECT Gender,avg(Usia) FROM data_table group by Gender'. engine)
print(res2)
#print ('')

#res2 = pd.read_sql_query('SELECT divisi,sum(gaji)  FROM data_table group by divisi', engine)
#print('result 2')
#print(res2)
#============================================

#============================================================
#sql.execute('INSERT INTO data_table VALUES(?,?,?,?,?,?)', engine, params=[('id',8,'guru',722.5, '08/01/2012','Finance')])
#res = pd.read_sql_query('SELECT ID,divisi,nama,gaji,tanggal FROM data_table', engine)
#print(res)
#===========================================================

#================================================
#sql.execute('Delete from data_table where nama = (?) ', engine, params=[('guru')])
#res = pd.read_sql_query('SELECT ID,divisi,nama,gaji,tanggal FROM data_table', engine)
#print(res)
#=====================================================


