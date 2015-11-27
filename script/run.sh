#########################################################################
# File Name: run.sh
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Sun 22 Nov 2015 02:41:53 PM CST
#########################################################################
#!/bin/bash

python split_data.py gd_6
python average_times.py 6 0
cd ../feature/
python all_feature.py
cd ../training/
python gbdt.py 6

cd ../script/
python split_data.py gd_11
python average_times.py 11 0
cd ../feature/
python all_feature.py
cd ../training/
python gbdt.py 11


cd ../script/
python join_line.py
