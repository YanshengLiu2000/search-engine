import sys
import numpy as np
from gensim import models
import pickle
from webapp import config
import os

"""
This file is used to load all models before the web server runs. 
So that all models can load once at the very beginning instead of load every search.
"""

print("This is load_models.py")
model = models.Doc2Vec.load(config.MODEL_DIR)
file_path = os.path.join(config.NECESSARY_DATA_DIR,
                         "filename_to_casename.pkl")  # use transfer filename to article's title
file = open(file_path, "rb")
file_to_case = pickle.load(file)
# =======================fast_query_part==============================
NECESSARY_DATA_DIR = config.NECESSARY_DATA_DIR
sys.path.append(config.FQ_DIR)
import lsh

# load all necessary parameters of lsh
dataset = np.load(config.DATASET_DIR)
lsh_test = lsh.LSH()
euclidean = False
number_of_tables = 1
hash_fx = 1
LSHtable = lsh_test.LSHtable(dataset, euclidean, number_of_tables, hash_fx)#new a lsh variable

file = open(os.path.join(NECESSARY_DATA_DIR, 'reverse_dictionary.pkl'), 'rb')
reverse_dictionary = pickle.load(file)
