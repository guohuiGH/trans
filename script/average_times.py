#########################################################################
# File Name: average_times.py
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Sun 15 Nov 2015 07:20:10 PM CST
#########################################################################
#!/usr/bin/bash
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
xianlu = ''

def parse_time(time):
    month = int(time[4:6])
    day = int(time[6:8])
    hour = time[8:]
    base = 0
    if month == 8:
        base = 0
    elif month == 9:
        base = 30
    elif month == 10:
        base = 61
    elif month == 11:
        base = 91
    elif month == 12:
        base = 122
    day = base + day
    return str(day), str(hour)

def read_data(file_name):
    global xianlu
    my_file = open(file_name)
    name_day_hour = dict()
    line = my_file.readline()
    while line:
        line_list = line.strip().split(',')
        line_name = line_list[1][6:]
        xianlu = line_list[1][0:6]
        deal_time = line_list[5]
        (day, hour) = parse_time(deal_time)
        s = line_name + ',' + day + ',' + hour
        if s not in name_day_hour.keys():
            name_day_hour[s] = 1
        name_day_hour[s] += 1
        line = my_file.readline()
    my_file.close()
    return name_day_hour

def get_average_week(name_day_hour):
    name_week_hour = dict()
    day_hours = name_day_hour.keys()
    for line in day_hours:
        line_list = line.split(',')
        line_list[1] = str(int(line_list[1])%7)
        name = ','.join(line_list)
        
        temp_list = list()
        if name in name_week_hour.keys():
            temp_list = name_week_hour[name]
        temp_list.append(name_day_hour[line])
        name_week_hour[name] = temp_list
    return name_week_hour

def get_max_min_aver(name_week_hour):
    name_week_hour_min = dict(); name_week_hour_max = dict(); name_week_hour_aver = dict();
    week_hours = name_week_hour.keys()
    for line in week_hours:
        temp_list = name_week_hour[line]
        name_week_hour_max[line] = max(temp_list)
        name_week_hour_min[line] = min(temp_list)
        name_week_hour_aver[line] = sum(temp_list)/len(temp_list)
    return name_week_hour_max, name_week_hour_min, name_week_hour_aver



def write_file(test_name_day_hour,file_name):
    global xianlu
    my_file = open(file_name, 'w+')
    name_list = test_name_day_hour.keys()
    for line in name_list:
        temp = ''
        nums = test_name_day_hour[line]
        line_list = line.split(',')
        line_list[0] = xianlu + line_list[0]
        line_list[1] = '2015010' + str(int(line_list[1]) +1)
        hour = line_list[2]
        if hour< '06'or hour > '21':
            continue
        temp = ','.join(line_list) + ',' + str(nums) + '\n'
        my_file.write(temp)
    my_file.close()
        
        


def main():
    train_file = '../tmp/gd_train'
    train_name_day_hour = read_data(train_file)
    train_name_week_hour = get_average_week(train_name_day_hour)
    (maxValue, minValue, averValue) = get_max_min_aver(train_name_week_hour)
    predict_file = '../tmp/predict_av.txt'
    write_file(averValue, predict_file)
    predict_file = '../tmp/predict_ma.txt'
    write_file(maxValue, predict_file)
    predict_file = '../tmp/predict_mi.txt'
    write_file(minValue, predict_file)
    test_file = '../tmp/gd_test'
    test_name_day_hour = read_data(test_file)
    predict_file = '../tmp/predict'
    write_file(test_name_day_hour,predict_file)


if __name__=='__main__':
    main()
