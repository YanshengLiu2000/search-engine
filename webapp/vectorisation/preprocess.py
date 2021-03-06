import os
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
import re



def preprocess(textfiles,train=0):

    parsed_directory = os.path.join(os.getcwd(),"parsed_data")
    # if not os.path.exists(parsed_directory):
    #     os.makedirs(parsed_directory)

    if type(textfiles) is list: #we assume a list of documents are being provided.


        for files in textfiles:
            fname = files.split('.')[0]
            if train == 1:
                files = os.path.join(os.getcwd(), "scraped_data",files)
            with open(files, 'r+',encoding='utf-8') as f:
                text = f.read()
                new_file_name = os.path.join(parsed_directory, fname+ ".txt")
                write_file = open(new_file_name, 'w')
                txt = " ".join(
                    [i for i in re.sub(r'[^a-z0-9A-Z\s]', "", text).lower().split() if i not in ENGLISH_STOP_WORDS])
                write_file.write(txt)
                write_file.close()
    else: #if it's not a list, it is probably as query string
        txt = " ".join(
            [i for i in re.sub(r'[^a-z0-9A-Z\s]', "", textfiles).lower().split() if i not in ENGLISH_STOP_WORDS])
        return txt


