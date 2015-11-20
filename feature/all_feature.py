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
    brefore_holiday=[38,61,153]
    holiday = [39,62,63,64,65,66,77,68]
    after_holiday = [72,157]
    for d in brefore_holiday:
        if day == d:
            return 1
    for d in holiday:
        if day == d:
            return 2
    for d in after_holiday:
        if day == d:
            return 3
    return 4

def connect_feature(file_name1, file_name2):
    file1 = open(file_name1)
    file2 = open(file_name2, 'w+')
    weather_feature = weather.get_weather()
    line = file1.readline()
    features = list()
    while line:
        temp_list = list()
        line_list = line.strip().split(',')
        temp_list.append(line_list[3])
        if line_list[0] == '10':
            temp_list.append('1')
        else:
            temp_list.append('2')
        day = int(line_list[1])
        temp_list.append(str(day%7 + 1))
        temp_list.append(str(isHoliday(day)))
        temp_list.append(str(int(line_list[2])))
        #print weather_feature[str(day)]
        temp_list.extend(weather_feature[str(day)][1:])
        features.append(','.join(temp_list))
        file2.write(','.join(temp_list) + '\n')
        line = file1.readline()
    file1.close()
    file2.close()
    return features

def max_range(features):
    col = len(features[0])
    maxlen = list()
    maxlen.append(0)
    for i in range(1, col):
        maxlen.append(max([line[i] for line in features]))
    return maxlen

def one_hot_encoding(file_name, features):
    file1 =open(file_name, 'w+')
    length = len(features)

    for i in range(0, length):
        features[i] = features[i].split(',') 
        for j in range(0,len(features[i])):
            features[i][j] = int(features[i][j])
    maxlen = max_range(features)    
    le = len(maxlen)

    sum_length = sum(maxlen)
    origin_list = list()
    for i in range(0,sum_length):
        origin_list.append('0')

    for i in range(0, length):
        temp_list = list()
        temp_list.append(str(features[i][0]))
        temp_list.extend(origin_list)


        for j in range(0, le-1):
            index = sum(maxlen[0:j+1]) + features[i][j+1]

            temp_list[index] = '1'
        file1.write(' '.join(temp_list) + '\n')

    file1.close()
    

def main():
    max_file = '../tmp/predict_ma.txt'
    min_file = '../tmp/predict_mi.txt'
    read_file(max_file, min_file)
    name_file = '../tmp/name_day_hour'
    feature_file = '../tmp/all_feature'
    features = connect_feature(name_file, feature_file)
    dense_file = '../tmp/feature_dense'
    one_hot_encoding(dense_file, features)

if __name__=='__main__':
    main()
