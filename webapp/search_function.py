import sys
import numpy as np
from webapp import config
from webapp import load_models

print("This is the  search_function.py!")

VEC_DIR = config.VEC_DIR
NECESSARY_DATA_DIR = config.NECESSARY_DATA_DIR
"""
This is script is used to link flask, vectorisation and fast query.
"""


def get_results(input_string, model, dataset):
    """
    :param input_string: target sentences
    :param model: used in doc2vec
    :param dataset: used in fast_query
    :return: search results

    This function receives the input information from website and give back a list of search results.
    Each elements in the result list is a dictionary which contains the
    """
    sys.path.append(VEC_DIR)
    import query
    doc_vector = query.get_query_vec(input_string,
                                     model)  # give input string to vectorisation part and use doc_vecor to get the vector
    file_to_case = load_models.file_to_case  # works perfect transfer from name.thml to article title.
    # ===============================fast_query_part========================================

    lsh_test = load_models.lsh_test
    LSHtable = load_models.LSHtable
    query = doc_vector
    k = 100  # how many results will be shown in the result page

    results = lsh_test.query(query, LSHtable, k)
    reverse_dictionary = load_models.reverse_dictionary

    max_num = 0
    min_num = 10000  # use to record the numpy similarity
    temp_result = []
    for rank, elem in enumerate(results):
        num = np.linalg.norm(query - dataset[elem])
        temp_dict = {
            'file_name': reverse_dictionary[elem].replace("txt", "html"),
            'article_title': file_to_case[reverse_dictionary[elem].replace("txt", "html")],
            'numpy_distance': num}
        temp_result.append(temp_dict)
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    output_result = sorted(temp_result,
                           key=lambda x: x['numpy_distance'])  # results sorted by numpy distance of the articles
    rank = 1
    for elem in output_result:
        elem['rank'] = rank  # add rank#
        elem['similarity'] = (1 - (elem['numpy_distance'] - min_num) / (max_num - min_num)) * 100#calculate the relative similarity
        elem['similarity'] = ("%.2f" % elem['similarity'])#siginificant digits
        rank += 1
    return output_result  # return the search result.


if __name__ == '__main__':
    print("This is the function test part:\r\n")
    test_string = ""

    with open('/home/da_comp9900/Documents/parsed_data/NSWSC_2002_22.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            test_string += line

    output_result = get_results(test_string, load_models.model, load_models.dataset)
    print(len(output_result))
    print(output_result)
    for elem in output_result:
        print(elem)
