#########################################################################
# File Name: split_line.py
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Sun 22 Nov 2015 02:27:21 PM CST
#########################################################################
#!/bin/bash
#coding=utf-8

def main():
    myfile = open('../tmp/gd_train_data.txt')    
    train_10 = open('../tmp/gd_6', 'w+')
    train_15 = open('../tmp/gd_11', 'w+')
    line = myfile.readline()
    while line:
        line_list = str(line).strip().split(',')
        name = line_list[1][6:]
        if line_list[5] < '2014090100':
            line = myfile.readline()
            continue
        if name == '6':
            train_10.write(str(line))
        elif name == '11':
            train_15.write(str(line))
        line = myfile.readline()
    myfile.close()
    train_10.close()
    train_15.close()

if __name__=='__main__':
    main()

