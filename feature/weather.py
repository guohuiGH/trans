#########################################################################
# File Name: get_weather.py
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Wed 18 Nov 2015 04:46:41 PM CST
#########################################################################
#!/bin/bash
#coding=utf-8

day_dic = dict()
wea_dic = dict(); count_wea = 1
tem_dic = dict(); count_tem = 1
win_dic = dict(); count_win = 1

def parse_time(time):
    month = int(time[1])
    day = int(time[2])
    base = 0
    if month == 8:
        base = 0
    elif month == 9:
        base = 31
    elif month == 10:
        base = 61
    elif month == 11:
        base = 92
    elif month == 12:
        base = 122
    elif month == 1:
        base = 153
    return str(base + day)

def parse_wea(weather):
    global wea_dic; global count_wea
    for i in range(0, len(weather)):
        w = weather[i]
        if w not in wea_dic.keys():
            wea_dic[w] = count_wea
            count_wea += 1
        weather[i] = str(wea_dic[w])
    return ','.join(weather)

def parse_tem(tmp):
    global tem_dic; global count_tem
    for i in range(0, len(tmp)):
        t = tmp[i]
        if t not in tem_dic.keys():
            tem_dic[t] = count_tem
            count_tem += 1
        tmp[i] = str(tem_dic[t])
    return ','.join(tmp)

def parse_win(windy):
    global win_dic; global count_win
    for i in range(0, len(windy)):
        w = windy[i]
        if w not in win_dic.keys():
            win_dic[w] = count_win
            count_win += 1
        windy[i] = str(win_dic[w])
    return ','.join(windy)
    

def read_file(file_name):
    myfile = open(file_name)
    line = myfile.readline()
    while line:
        line_list = str(line).strip().split(',')
        line_list[0] = parse_time(line_list[0].split('/'))
        line_list[1] = parse_wea(line_list[1].split('/'))
        line_list[2] = parse_wea(line_list[2].split('/'))
        line_list[3] = parse_win(line_list[3].split('/'))
        day_dic[line_list[0]] = (line_list)
        line = myfile.readline()
    myfile.close()
    #print len(day_dic)
    return day_dic


def get_weather():
    weather_file = '../tmp/gd_weather_report.txt'
    return read_file(weather_file)

if __name__ == '__main__':
    main()    
