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
    holiday = [39,62,63,64,65,66,77,68,154,155,156]
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
        #if line_list[0] == '10':
        #    temp_list.append('1')
        #else:
        #   temp_list.append('2')
        day = int(line_list[1])
        holiday = isHoliday(day)
        if holiday == 2:
            temp_list.append(str(2))
            temp_list.append(str(8))
        elif holiday == 3:
            if day == 157:
                temp_list.append(str(1))
                temp_list.append(str(1))
            elif day == 72:
                temp_list.append(str(1))
                temp_list.append(str(5))
        elif holiday == 1:
            temp_list.append(str(1))
            temp_list.append(str(day%7 + 1))
        elif holiday == 4:
            if day %7 > 0 and day %7 < 6:
                temp_list.append(str(1))
                temp_list.append(str(day%7))
            elif day % 7 == 0:
                temp_list.append(str(2))
                temp_list.append(str(7))
            elif day %7 == 6:
                temp_list.append(str(2))
                temp_list.append(str(6))

        #temp_list[1] = (str(day%7 + 1))
        #temp_list[2] = (str(isHoliday(day)))
        temp_list.append(str(int(line_list[2])-5))
        #print weather_feature[str(day)]
        temp_list.extend(weather_feature[str(day)][1:])
        features.append(','.join(temp_list))
        file2.write(','.join(temp_list) + '\n')
        line = file1.readline()
    file1.close()
    file2.close()
    return features

def change_features(features):

    length = len(features)
    for i in range(0, length): 
        features[i] = features[i].split(',') 
        for j in range(0,len(features[i])):
            features[i][j] = int(features[i][j])
    maxlen = max_range(features)
    return features, maxlen
    

def max_range(features):
    col = len(features[0])
    maxlen = list()
    maxlen.append(0)
    for i in range(1, col):
        maxlen.append(max([line[i] for line in features]))
    return maxlen

def one_hot_encoding(file_name, features, maxlen):
    file1 =open(file_name, 'w+')
    le = len(maxlen)
    sum_length = sum(maxlen)
    origin_list = list()
    for i in range(0,sum_length):
        origin_list.append('0')
    length = len(features)
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
    name_file = '../tmp/name_day_hour_train'
    feature_file = '../tmp/train_feature'
    features = connect_feature(name_file, feature_file)
    (train_features, maxlen1) = change_features(features)
    
    name_file = '../tmp/name_day_hour_validation'
    feature_file = '../tmp/validation_feature'
    features = connect_feature(name_file, feature_file)
    (validation_features, maxlen2) = change_features(features)

    name_file = '../tmp/name_day_hour_test'
    feature_file = '../tmp/test_feature'
    features = connect_feature(name_file, feature_file)
    (test_features, maxlen3) = change_features(features)

    maxlen = max(maxlen1, max(maxlen2, maxlen3))
    print maxlen
    dense_file = '../tmp/feature_dense_train'
    one_hot_encoding(dense_file, train_features, maxlen)

    dense_file = '../tmp/feature_dense_validation'
    one_hot_encoding(dense_file, validation_features, maxlen)

    dense_file = '../tmp/feature_dense_test'
    one_hot_encoding(dense_file, test_features, maxlen)

if __name__=='__main__':
    main()
