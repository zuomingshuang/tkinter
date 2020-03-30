import pandas as pd
import xlrd
import pymysql

conn=pymysql.connect('localhost','root','123','zms')

dt=pd.read_excel(r'C:\\Users\\Lenovo\\Desktop\\店铺.xlsx')
dt.to_sql(name='aa',con=conn)
print(dt)