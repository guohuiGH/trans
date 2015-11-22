#########################################################################
# File Name: run.sh
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Sun 22 Nov 2015 02:41:53 PM CST
#########################################################################
#!/bin/bash

python split_data.py gd_10
python average_times.py 10 0
cd ../feature/
python all_feature.py
cd ../training/
python linear_rs.py 10

cd ../script/
python split_data.py gd_15
python average_times.py 15 0
cd ../feature/
python all_feature.py
cd ../training/
python linear_rs.py 15
