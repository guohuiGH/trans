
def main():
    myfile = open('../tmp/gd_train_data.txt')
    line = myfile.readline()
    line_dic = dict()
    while line:
        line_list = str(line).strip().split(',')
        if line_list[1] not in line_dic:
            line_dic[line_list[1]] = 1
        line = myfile.readline()
    myfile.close()
    print line_dic

if __name__=='__main__':
    main()
