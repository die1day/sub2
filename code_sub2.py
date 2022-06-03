# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 07:19:42 2022

@author: Jeff
"""

import pandas as pd
import os

def get_table():
    # path = r'..\main\data'
    path = r'C:\Users\Jeff\git_test\main\data'
    
    filepath = os.path.join(path, 'table.csv')
    
    df = pd.read_csv(filepath)
    print(df)