import numpy as np
import falconn
import timeit
from scipy.spatial import distance


class LSH:
    """
    Local-Sensitivity Hashing (LSH) is a class of methods for the nearest neighbor search problem.

    https://github.com/FALCONN-LIB/FALCONN
    """

    def LSHtable(self, file, euclidean=True, number_of_tables=50, hash_fx=18):
        """
        input:                  2-D numpy array
        output:                 LSH table

        Params:
        :file:                  2-D numpy array of document vectors
        :distance_function:     [EuclideanSquared, NegativeInnerProduct]
        :number_of_tables:      (default=50)
        :num_of_rotations:      1
        :seed:                  5721840
        :num_setup_threads:     0
        :hash_fx:               18 (2^18 hash tables)

        """
        dataset = file
        params_cp = falconn.LSHConstructionParameters()
        params_cp.dimension = len(dataset[0])
        params_cp.lsh_family = falconn.LSHFamily.CrossPolytope
        if euclidean == True:
            params_cp.distance_function = falconn.DistanceFunction.EuclideanSquared
        else:
            params_cp.distance_function = falconn.DistanceFunction.NegativeInnerProduct
        params_cp.l = number_of_tables
        params_cp.num_rotations = 1
        params_cp.seed = 5721840
        params_cp.num_setup_threads = 0
        params_cp.storage_hash_table = falconn.StorageHashTable.BitPackedFlatHashTable
        falconn.compute_number_of_hash_functions(hash_fx, params_cp)
        # Construct the LSH table
        LSHtable = falconn.LSHIndex(params_cp)
        LSHtable.setup(dataset)
        return LSHtable

    def query(self, query, LSHtable, k=100, number_of_probes=54000):
        """
        input:                  1-D document vector
        output:                 array of element results

        Params:
        :query:                 1-D document vector
        :LSHtable:              LSH table
        :k:                     number of nearest neighbors (default=100)
        :number_of_probes:      54000 (fine tuned parameter)

        """
        # transformed_query = self.transform(query)
        query_object = LSHtable.construct_query_object()
        query_object.set_num_probes(number_of_probes)
        return query_object.find_k_nearest_neighbors(query, k)

    def transform(self, dataset):
        """
        Normalizing and centering the data has no effect in correctness, but signifcantly speeds the LSH algorithm.

        input:                  dataset
        output:                 transformed dataset
        """
        # Normalize the dataset
        dataset /= np.linalg.norm(dataset, axis=0)
        # dataset /= np.linalg.norm(dataset, axis=1).reshape(-1, 1)
        # Center the data
        center = np.mean(dataset, axis=0)
        dataset -= center
        return dataset


if __name__ == '__main__':

    # load file and create query
    import numpy as np

    file = "../static/add_files_here/similarity_matrix.npy"

    # create instance of LSH class
    lsh = LSH()

    # table parameters
    starttime1 = timeit.timeit()
    dataset = np.load(file)
    endtime1 = timeit.timeit()
    print("test load matrix part ",endtime1 - starttime1)
    number_of_tables = 50
    euclidean = True

    # create table
    starttime2 = timeit.timeit()
    LSHtable = lsh.LSHtable(dataset, euclidean, number_of_tables)
    endtime2 = timeit.timeit()
    print("build table part ",endtime2 - starttime2)

    # query parameters
    query = dataset[24312]
    k = 100

    # run query and return query run time
    starttime = timeit.timeit()
    results = lsh.query(query, LSHtable, k, number_of_tables)
    endtime = timeit.timeit()

    # print output
    print("Run time: {:0.6f}".format(endtime - starttime))
    print("{:>5}{:>6}{:>20}{:>20}".format("rank", "elem", "numpy distance", "sklearn distance"))
    for rank, elem in enumerate(results):
        print("{:>5}{:>6}{:>20}{:>20}".format(rank, elem, np.linalg.norm(query - dataset[elem]),
                                              distance.euclidean(query, dataset[elem])))