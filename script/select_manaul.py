#########################################################################
# File Name: select_manaul.py
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Fri 20 Nov 2015 12:09:15 AM CST
#########################################################################
#!/bin/bash
#coding=utf-8

def read_file():
    xianlu = ''
    f1 = open('../tmp/temp.txt', 'w+')
    f2 = open('../tmp/predict_av.txt')
    line = f2.readline()
    name_day_hour = dict()
    while line:
        line_list = line.strip().split(',')
        xianlu = line_list[0][0:6]
        if line_list[1] >= '20150104':
            f1.write(line)
        name = ','.join(line_list[0:len(line_list)-1])
        name_day_hour[name] = line_list[len(line_list)-1]
        line = f2.readline()
    f2.close()

    f3 = open('../tmp/name_day_hour')
    line = f3.readline()
    while line:
        line_list = line.strip().split(',')
        line_list[0] = xianlu + line_list[0]
        if line_list[1] == '62':
            line_list[1] = '20150101'
        elif line_list[1] == '63':
            line_list[1] = '20150102'
        elif line_list[1] == '64':
            line_list[1] = '20150103'
       # elif line_list[1] == '72':
        #    line_list[1] = '20150104'
        else:
            line = f3.readline()
            continue
        if line_list[2] > '21' or line_list[2] < '06':
            line = f3.readline()
            continue
        f1.write(','.join(line_list) + '\n')
        line = f3.readline()
    f3.close()
    f1.close()

    f4 = open('../tmp/manaual_predict.txt', 'w+')
    f1 = open('../tmp/temp.txt')
    line = f1.readline()
    while line:
        line_list = line.strip().split(',')
        
        s = str(int(line_list[1])+1)
        name = line_list[0] + ',' + s + ',' + line_list[2]

        if line_list[1] == '20150104':
            #print name
            line_list[len(line_list)-1] = name_day_hour[name]
        f4.write(','.join(line_list) + '\n')
        line = f1.readline()
    f1.close()
    f4.close()

    




def main():
    read_file()

if __name__=='__main__':
    main()
