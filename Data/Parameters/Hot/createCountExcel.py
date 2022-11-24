# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 21:23:29 2022

@author: mohsen
"""
import os
import pandas as pd




path ="C:\Thesis\Code"

os.chdir(path)
data = pd.read_excel('syndrome-report 1394-1397.xlsx',sheet_name="تنفسی",)
df = pd.DataFrame(data)

column = data['شبکه بهداشت']
print (type(column))
test = df.groupby('شبکه بهداشت').size()
test.to_frame(name='تعداد').to_excel('count.xlsx', sheet_name='Main')