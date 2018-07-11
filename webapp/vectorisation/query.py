import preprocess
from sklearn.decomposition import PCA
from numpy import zeros, random, sum as np_sum, add as np_add, concatenate, \
    repeat as np_repeat, array, float32 as REAL, empty, ones, memmap as np_memmap, \
sqrt, newaxis, ndarray, dot, vstack, dtype, divide as np_divid
from gensim import matutils



def get_query_vec(query,model):

    normalized_query = preprocess.preprocess(query)


    if len(normalized_query) < 7: #if the query string contains less than 7 words, then find the mean of their vectors
        mean = []
        wordlist = normalized_query.split()
        for word in wordlist:
            try:
                mean.append(model[word])
            except KeyError:  #if the word has a spelling mistake or is not in the dictionary
                pass

        try:
            query_vector = matutils.unitvec(array(mean).mean(axis=0)).astype(REAL) #compute the mean vector for all the words
        except TypeError: #if only 1 word was queried and that word wasn't in the dictionary
            query_vector = 0
        return query_vector

    else:
        model.random.seed(0)
        query_vector = model.infer_vector(normalized_query.split(),alpha=0.025,steps=25) # try adjusting the parameters here
        return  query_vector


