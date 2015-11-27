#########################################################################
# File Name: adjust_value.py
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Thu 26 Nov 2015 02:25:50 PM CST
#########################################################################
#!/bin/bash
#coding=utf-8


def read_file():
    xianlu = ''

    f2 = open('../tmp/test_predict.txt')
    name_dict = dict()
    line = f2.readline() 
    while line:
        line_list = line.strip().split(',')
        name = ','.join(line_list[0:len(line_list)-1])
        name_dict[name] = line_list[len(line_list)-1]
        line = f2.readline()
    f2.close()

    

    f4 = open('../tmp/predict.txt', 'w+')
    f1 = open('../tmp/test_predict.txt')
    line = f1.readline()
    while line:
        line_list = line.strip().split(',')
        s = str(int(line_list[1])+1)
        name = line_list[0] + ',' + s + ',' + line_list[2]

        if line_list[1] == '20150104':
            #print name
            line_list[len(line_list)-1] = name_dict[name]
        f4.write(','.join(line_list) + '\n')
        line = f1.readline()
    f1.close()
    f4.close()

    




def main():
    read_file()

if __name__=='__main__':
    main()
