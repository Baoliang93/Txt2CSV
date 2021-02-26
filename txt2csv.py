#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:24:04 2021

@author: blchen
"""
import pandas as pd

def getNumTxt (txtname):
    ftest=open(txtname,'r')
    f=open('temp.txt',"w")
    data=ftest.readlines()  
    
    for i in range(len(data)):
        Flag = False
        for j in range(len(data[i])):
            temp = data[i][j]
            if temp in ['0','1','2','3','4','5','6','7','8','9','.']: 
               Flag = True
               f.write(temp)
            elif Flag ==True and temp!='\n' :
               f.write(',')
               Flag = False
            else:
               Flag = False              
        f.write('\n')         
    f.close() 


   
if __name__ == '__main__':
    txtname = 'test.txt'
    getNumTxt(txtname)
    data = pd.read_csv('temp.txt',header=None)
#    data = pd.read_csv('temp.txt',names= ['a', 'b', 'c', 'd','e'])
    print(data)
    data.to_csv('data.csv', header= 0)
