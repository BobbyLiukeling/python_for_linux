#!/usr/bin/env python
# encoding: utf-8
'''
@author: bobby
@file: data_to_mysql.py
@time: 7/22/20 12:05 AM
'''


import pymysql
import numpy as py
import pandas as pd
import pdb

class Insert_to_Mysql:
    def __init__(self):
        self.db = pymysql.connect( #连接数据库
            host = '127.0.0.1',
            port = 3306,
            user = 'bobby',
            password = '520lkl',
            db = 'CRISPR',
            charset = 'utf8',
        )

        self.coursr = self.db.cursor() #创建一个游标对象

    def xsl_to_csv(self):
        '''
        读入数据并将数据规范化
        :return:
        '''
        df = pd.read_excel('Cas9.xlsx')
        df.rename(columns={
            'Abrevation (3 let)':'CRISPR_name','Clade':'type','Length':'CRISPR_Length','PAM (consensus)':'PAM_Consensus',
            'Cas9 AA sequence':'CRISPR_Consensus','PI domain sequence':'PI_Sequence',
        },inplace=True)
        df = df.drop(labels='No', axis=1) #删除序号
        df = df.dropna()
        df = df.drop_duplicates()
        df['PI_Length'] = df['PI_Sequence'].str.len() #comput the length of PI_sequence
        df['CRISPR_Length'] = df['CRISPR_Length'].apply(lambda x:int(x))
        df['PI_Length'] = df['PI_Length'].apply(lambda x:int(x))
        df['PI_Start_Position'] = df['CRISPR_Length']-df['PI_Length']+1 #the start position of PAM sequence in CRISPR_senquence
        print('OK')







if __name__ == "__main__":
    Main = Insert_to_Mysql()
    Main.xsl_to_csv()








