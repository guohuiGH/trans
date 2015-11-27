#########################################################################
# File Name: run_manaual.sh
# Author: guohui
# mail: guohui1029@foxmail.com
# Created Time: Fri 27 Nov 2015 11:11:46 AM CST
#########################################################################
#!/bin/bash
#coding=utf-8
python split_data.py gd_6
python average_times.py 6 0
python select_manaul.py 6

python split_data.py gd_11
python average_times.py 11 0
python select_manaul.py 11


python join_line.py
