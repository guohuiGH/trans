#########################################################################
# File Name: all_feature.py
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Wed 18 Nov 2015 08:31:51 PM CST
#########################################################################
#!/bin/bash
#coding=utf-8

import weather

def read_file(file_name1, file_name2):
    file1 = open(file_name1)
    file2 = open(file_name2)
    length = len(file1.readline().strip().split(','))
    lines = file2.readlines()
    maxValue = [ int(line.strip().split(',')[length-1]) for line in lines]
    file1.close()
    file2.close()
    return maxValue

def isHoliday(day):
    if day == 

def connect_feature(file_name1, maxValue, file_name2):
    file1 = open(file_name1)
    file2 = open(file_name2, 'w+')
    weather_feature = weather.get_weather()
    line = file1.readline()
    while line:
        temp_list = list()
        line_list = line.strip().split(',')
        temp_list.append(line_list[0])
        temp_list.append(str(int(line_list[1])%7))

    
    

def main():
    max_file = '../tmp/predict_ma.txt'
    min_file = '../tmp/predict_mi.txt'
    read_file(max_file, min_file)
    name_file = '../tmp/name_day_hour'
    connect_feature(name_file)

if __name__=='__main__':
    main()
