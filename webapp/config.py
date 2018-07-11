import os

"""
This file stores all necessary directory may be used in other part of project.
"""
print("this is config.py.")
ROOT_DIR = os.path.dirname(__file__)  # directory of the project root
VEC_DIR = os.path.join(ROOT_DIR, 'vectorisation')  # store all vectorisation part
FQ_DIR = os.path.join(ROOT_DIR, 'fast_query')  # store all fast query part
NECESSARY_DATA_DIR = os.path.join(os.path.join(ROOT_DIR, 'static'), 'models')  # store all models and model files
MODEL_DIR = os.path.join(os.path.join(os.path.join(ROOT_DIR, 'static'), 'models'),
                         'doc2vec.model')  # directory of doc2vec.model
UPLOAD_FOLDER_DIR = os.path.join(os.path.join(ROOT_DIR, 'static'), 'upload')  # upload folder
DATASET_DIR = os.path.join(os.path.join(os.path.join(ROOT_DIR, 'static'), 'models'),
                           'similarity_matrix.npy')  # directory of similarity_matrix.npy
NSW_DIR = os.path.join(os.path.join(os.path.join(ROOT_DIR, 'static'), 'models'), 'NSWSC')  # store all articles in html.
