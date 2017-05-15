#!/usr/bin/env python
# Filename: delete_csv_column 
"""
introduction:

authors: Huang Lingcao
email:huanglingcao@gmail.com
add time: 24 April, 2017
"""

from optparse import OptionParser
import basic, io_function

import csv

def delete_fouth_coloumn_csv(csv_path):

    with open(csv_path, 'rb') as f:
        reader = csv.reader(f)
        input_list = map(tuple, reader)
        f.close()
    save_path = io_function.get_name_by_adding_tail(csv_path,'modify')
    save_csv=open(save_path,'wb')
    csv_writer = csv.writer(save_csv)

    number = 1
    for line in input_list:
        # if number ==1:
        #     number = number+1
        #     continue
        number = number + 1
        save_ele = list(line)
        # line[3] = str(1)
        save_ele[3] = str(1)
        csv_writer.writerows([save_ele])
        # csv_writer.writerows([line])

    save_csv.close()

    return save_path

def merge_AOI_result_csv(file_list,output):

    save_csv = open(output, 'wb')
    csv_writer = csv.writer(save_csv)
    for csv_file in file_list:
        with open(csv_file, 'rb') as f:
            reader = csv.reader(f)
            input_list = map(tuple, reader)
            f.close()
        # number = 1
        for line in input_list:
            # if number ==1:
            #     number = number+1
            #     continue
            # number = number + 1
            save_ele = list(line)

            # if save_ele[0].find('AOI')<0:
            #     continue

            # line[3] = str(1)
            # save_ele[3] = str(1)
            csv_writer.writerows([save_ele])
            # csv_writer.writerows([line])

    save_csv.close()

    pass

def main(options, args):

    path_list = args
    # path = 'result_buildings.csv'
    modify_list = []
    for path in path_list:
        m_path = delete_fouth_coloumn_csv(path)
        modify_list.append(m_path)

    merge_AOI_result_csv(modify_list,'result_buildings_Test_public.csv')

    pass




if __name__=='__main__':
    usage = "usage: %prog [options] csv_file ... "
    parser = OptionParser(usage=usage, version="1.0 2017-4-24")

    (options, args) = parser.parse_args()
    if len(args) <1:
        parser.print_help()
        exit(1)

    main(options, args)

    print ('finished')