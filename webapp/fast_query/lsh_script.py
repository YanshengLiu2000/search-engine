import numpy as np
import falconn
import timeit
# import math
from os import listdir


datadir = "../data_vectors"
dataset_file = datadir + '/matrix_model.npy'
number_of_tables = 50

parsed_files_dir = datadir +'/parsed_data'


# Read the dataset
dataset = np.load(dataset_file)

# Normalize the dataset
dataset /= np.linalg.norm(dataset, axis=1).reshape(-1, 1)

# Center the data
center = np.mean(dataset, axis=0)
dataset -= center

# Parameters
params_cp = falconn.LSHConstructionParameters()
params_cp.dimension = len(dataset[0])
params_cp.lsh_family = falconn.LSHFamily.CrossPolytope
params_cp.distance_function = falconn.DistanceFunction.EuclideanSquared
# params_cp.distance_function = falconn.DistanceFunction.NegativeInnerProduct
params_cp.l = number_of_tables
# we set one rotation, since the data is dense enough,
# for sparse data set it to 2
params_cp.num_rotations = 1
params_cp.seed = 5721840
# we want to use all the available threads to set up
params_cp.num_setup_threads = 0
params_cp.storage_hash_table = falconn.StorageHashTable.BitPackedFlatHashTable
# we build 18-bit hashes so that each table has
# 2^18 bins; this is a good choise since 2^18 is of the same
# order of magnitude as the number of data points
falconn.compute_number_of_hash_functions(18, params_cp)


starttime = timeit.timeit()
# Construct the LSH table
table = falconn.LSHIndex(params_cp)
table.setup(dataset)

number_of_probes = number_of_tables
query_object = table.construct_query_object()
query_object.set_num_probes(number_of_probes)

query = dataset[0]
result = query_object.find_k_nearest_neighbors(query, 100)
endtime = timeit.timeit()

print("runtime: %.6f" % (endtime - starttime))
print(result)

docLabels = [f for f in listdir(parsed_files_dir)]

for elem in result:
    print(elem, docLabels[elem], np.dot(query, dataset[elem]))