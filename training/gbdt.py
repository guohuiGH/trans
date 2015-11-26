#########################################################################
# File Name: gbdt.py
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Wed 25 Nov 2015 11:46:18 PM CST
#########################################################################
#!/bin/bash

from numpy import *
from sklearn.ensemble import GradientBoostingRegressor
import sys
def load_data_set(file_name):
    myfile = open(file_name)
    lines = myfile.readlines()
    labelMat = list(); dataMat = list()
    for line in lines:
        line_list = line.strip().split(' ')
        for i in range(len(line_list)):
            line_list[i] = float(line_list[i])
        labelMat.append(line_list[0])
        dataMat.append(line_list[1:])
    myfile.close()
    return dataMat, labelMat

def gbdt(dataMat, labelMat, testMat):
    xMat = mat(dataMat); yMat = ravel(labelMat); xxMat = mat(testMat)
    rsp = GradientBoostingRegressor(loss='ls', learning_rate=0.1, n_estimators=200,max_depth=4)
    rsp.fit(xMat, yMat)
    y = rsp.predict(testMat)
    print y
    return y

def write_file(file_name, y):
    myfile = open('../tmp/test_predict_' + str(file_name), 'w+')
    for i in y:
        myfile.write(str(int(i)) + '\n')
    myfile.close()



def main():
    data_set_file = '../tmp/feature_dense_train'
    (dataMat, labelMat) = load_data_set(data_set_file)
    
    data_set_file = '../tmp/feature_dense_test'
    (testXMat, testLabelMat) = load_data_set(data_set_file)
    y = gbdt(dataMat, labelMat, testXMat)
    
    write_file(sys.argv[1], y)
    
if __name__=='__main__':
    main()

