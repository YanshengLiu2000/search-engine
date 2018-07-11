import csv
import os
import sys

sys.path.append('..')

from webapp import search_function
from webapp import load_models


PARSED_DATA_DIR = '/home/itayfeldman/Documents/education/unsw/18s1/comp9900/slc-search-engine/parsed_data/'

def read_file(fx):
    content_string = ""
    with open(fx,'r') as fx:
        lines = fx.readlines()
        for l in lines:
            content_string += l
    return content_string

for idx, f in enumerate(os.listdir(PARSED_DATA_DIR)):
    fx = PARSED_DATA_DIR + f
    if os.stat(fx).st_size > 0:
        file = read_file(fx)
        print(idx, f)
        output_result = search_function.get_results(file, load_models.model, load_models.dataset)

        for elem in output_result:
            if elem['file_name'].replace('html', 'txt') == f:

                with open('lsh_result.csv', 'a+') as o:
                    writer = csv.writer(o)
                    writer.writerow([str(idx), f, str(elem['rank'])])
