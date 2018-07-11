#!/usr/bin/python3


from __future__ import print_function
import numpy as np
import sys
from os import listdir
import struct
import gensim

matrix = []
project_dir = '/home/itayfeldman/Documents/projects/slc-search-engine'
dataset_dir = '/data_vectors'
dataset_file = '/doc2vec.model'
parsed_files_dir = project_dir + dataset_dir +'/parsed_data'

docLabels = [f for f in listdir(parsed_files_dir)]

model = gensim.models.Doc2Vec.load(project_dir + dataset_dir + dataset_file)

for doc in docLabels:
    matrix.append(np.array(model[doc], dtype=np.float32))
np.save('matrix_model', np.array(matrix))

