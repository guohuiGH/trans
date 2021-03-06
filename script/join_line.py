#########################################################################
# File Name: join_line.py
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Sun 22 Nov 2015 05:22:48 PM CST
#########################################################################
#!/bin/bash
#coding=utf-8

def read_file(file_name):
    myfile = open(file_name)
    lines = myfile.readlines()
    myfile.close()
    return  [line.strip() for line in lines]
    

def write_file(file_name, line_nums):
    myfile = open(file_name, 'w+')
    myfile2 = open('../tmp/gd_6')
    xianlu = (myfile2.readline()).strip().split(',')[1][0:6]

    myfile2.close()
    count = 0
    for i in range(0,2):
        for j in range(1,8):
            for t in range(6,22):
                line = list()
                if i == 0:
                    line.append(xianlu + '6')
                elif i== 1:
                    line.append(xianlu + '11')
                line.append('2015010' + str(j))
                line.append((str(t)).zfill(2))
                line.append(line_nums[count])
                count +=1
                myfile.write(','.join(line) + '\n')
    myfile.close()

def sort_name(file_name, file_name2):
    myfile = open(file_name)
    name_dict = dict()
    line = myfile.readline()
    while line:
        line_list = line.strip().split(',')
        name = ','.join(line_list[0:len(line_list)-1])
        name_dict[name] = line_list[len(line_list)-1]
        line = myfile.readline()
    myfile.close()
    myfile = open(file_name2, 'w+')
    temp = name_dict.keys()
    temp.sort()
    for item in temp:
        myfile.write(item + ',' + name_dict[item] + '\n')
    myfile.close()

def main():

    file_name = '../tmp/test_predict_6'
    line_10 = read_file(file_name)
    file_name = '../tmp/test_predict_11'
    line_15 = read_file(file_name)
    file_name = '../tmp/test_predict2.txt'
    line_10.extend(line_15)
    write_file(file_name, line_10)
    
    
if __name__=='__main__':
    main()
