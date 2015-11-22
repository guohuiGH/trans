#########################################################################
# File Name: split_data.py
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Sun 15 Nov 2015 04:49:15 PM CST
#########################################################################
#!/bin/bash
#coding=utf-8

import sys

def main(line_name):
    myfile = open('../tmp/' + line_name)
    train_file = open('../tmp/gd_train', 'w+')
    test_file = open('../tmp/gd_validation', 'w+')

    line = myfile.readline()
    count = 0
    while line:
        line_list = str(line).strip().split(',')
        time = int(line_list[5])
        if time > 2014122500:
            test_file.write(str(line))
        else:
            train_file.write(str(line))
        line = myfile.readline()
    myfile.close()


if __name__=='__main__':
    main(sys.argv[1])

