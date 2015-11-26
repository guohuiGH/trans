#########################################################################
# File Name: linear_rs.py
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Sat 21 Nov 2015 12:41:16 AM CST
#########################################################################
#!/bin/bash
#coding=utf-8

from numpy import *

lam = -0.001

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
    global lam
    xMat = mat(xArr); yMat =  mat(yArr).T
    xTx = xMat.T*xMat + eye(shape(xMat)[1]) * lam 
    if linalg.det(xTx) == 0.0:
        print "matrix singular"
        return

    weight = xTx.I*(xMat.T*yMat)
    return weight

def predict(xArr, yArr, weight):
    global lam
    xMat = mat(xArr); 
    p_y = xMat*weight.tolist()
    print p_y
    loss = 0.0
    for i in range(0, len(yArr)):
        loss += (yArr[i] - p_y[i])*(yArr[i]- p_y[i])
    print loss

def main():
    data_set_file = '../tmp/feature_dense_train' 
    (dataMat, labelMat) = load_data_set(data_set_file)
    weight = linear_rs(dataMat, labelMat)

    data_set_file = '../tmp/feature_dense_validation'
    (vaMat, labelMat) = load_data_set(data_set_file)
    predict(vaMat, labelMat, weight)


if __name__=='__main__':
    main()
