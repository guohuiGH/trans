#########################################################################
# File Name: all_feature.py
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Wed 18 Nov 2015 08:31:51 PM CST
#########################################################################
#!/bin/bash
#coding=utf-8

import weather

def connect_feature(file_name):
    myfile = open(file_name)
    
    

def main():
    max_file = '../tmp/predict_ma.txt'
    min_file = '../tmp/predict_mi.txt'
    read_file()
    name_file = '../tmp/name_day_hour'
    connect_feature(name_file)

if __name__=='__main__':
    main()
