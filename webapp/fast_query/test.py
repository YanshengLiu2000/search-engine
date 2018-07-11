# load file and create query
import timeit
from os import listdir
import numpy as np
import lsh
from scipy.spatial import distance
import os

test1=os.path.dirname(os.getcwd())
test2=os.path.abspath(os.path.join(test1,'fast_query'))
test3=os.path.abspath(os.path.join(test1,'vectorisation'))
# print(test2)
# print(test3)
# print(os.getcwd())
import sys
sys.path.append(test3)
import query

test_result=query.get_query_vec("This is a long string. It used to test the fast query and vectorisation parts. and chek"
                                "if it works well")
print(test_result)
print(type(test_result))



file = "../data_vectors/matrix_model.npy"
parsed_files_dir="../data_vectors/parsed_data"
# create instance of LSH class
lsh_test = lsh.LSH()

# table parameters
dataset = np.load(file)
number_of_tables = 50
euclidean = True

# create table
LSHtable = lsh_test.LSHtable(dataset, euclidean, number_of_tables)

# query parameters
# query = dataset[0]  # this can be get from Daniel
query=test_result
k = 10  # try k=100
# print("test===============================", dataset[0])
# run query and return query run time
starttime = timeit.timeit()
results = lsh_test.query(query, LSHtable, k, number_of_tables)
endtime = timeit.timeit()

# print output
print("Run time: {:0.6f}".format(endtime - starttime))
print("{:>5}{:>6}{:>20}{:>20}".format("rank", "elem", "numpy distance", "sklearn distance"))
for rank, elem in enumerate(results):
    print("{:>5}{:>6}{:>20}{:>20}".format(rank, elem, np.linalg.norm(query - dataset[elem]),distance.euclidean(query, dataset[elem])))

docLabels = [f for f in listdir(parsed_files_dir)]
for elem in results:
    print(elem, docLabels[elem], np.dot(query, dataset[elem]))
