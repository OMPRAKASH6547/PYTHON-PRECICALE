# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 08:52:10 2021

@author: ompra
"""

import psycopg2  as ps

connection=ps.connect(
    host='localhost',
    database='myschool',
    user='postgres',
    password='12321',
    port='5432'
    
)
mycursor = connection.cursor()

qury="select * from student"


p="mycursor.execute(qury)"
print(p)


connection.commit()
connection.close()
