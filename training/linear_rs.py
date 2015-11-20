#########################################################################
# File Name: linear_rs.py
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Sat 21 Nov 2015 12:41:16 AM CST
#########################################################################
#!/bin/bash
#coding=utf-8

from numpy import *

def load_data_set(file_name):
    myfile = open(file_name)
    lines = myfile.readlines()
    labelMat = list(); dataMat = list()
    for line in lines:
        line_list = line.strip().split(' ')
        for i in range(0, len(line_list)):
            line_list[i] = float(line_list[i])
        labelMat.append(line_list[0])
        dataMat.append(line_list[1:])
    myfile.close()
    return dataMat, labelMat

def linear_rs(xArr, yArr):
    xMat = mat(xArr); yMat =  mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print "matrix singular"
        return
    weight = xTx.I*(xTx.T*yMat)
    return weight

def main():
    data_set_file = '../tmp/all_feature' 
    (dataMat, labelMat) = load_data_set(data_set_file)
    linear_rs(dataMat, labelMat)


if __name__=='__main__':
    main()
