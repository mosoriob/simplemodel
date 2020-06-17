#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:17:04 2020

@author: deborahkhider

Simple line model for testing MIC
"""

import json
import sys
import numpy as np
import os


def calc_predict(x,a,b,c):
    y=a*x+b+c
    return y

if __name__ == "__main__":
    with open(sys.argv[1]) as json_file:
        config=json.load(json_file)
    #open 
    dataset_name = config['input']['dataset_name']    
    dir_out = config['output']['path']
    a=float(config['params']['a'])
    b=float(config['params']['b'])
    c=float(config['params']['c'])
    #open the file
    x=np.genfromtxt('x.csv')[1:]
    #calculate
    y=calc_predict(x,a,b,c)
    #save as csv
    if dir_out[-1]=='/':
        if os.path.isdir(dir_out+'results') is False:
            os.makedirs(dir_out+'results')
    else:
        if os.path.isdir(dir_out+'/results') is False:
            os.makedirs(dir_out+'/results')
    path=dir_out+'/results/y.csv'
    np.savetxt(path,y)
    

