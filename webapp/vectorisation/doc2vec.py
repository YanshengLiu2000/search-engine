import gensim
from os import listdir
import os
import DocIterator as DocIt
import numpy as np
from sklearn.decomposition import PCA
import pickle

current_working_directory = os.getcwd()
doc2vec_dir = os.path.join(os.getcwd(),"doc2vec")
if not os.path.exists(doc2vec_dir):
    os.makedirs(doc2vec_dir)

docLabels = [f for f in listdir(os.path.join(os.getcwd(),"parsed_data")) ]

docData = []

for doc in docLabels:
    with open(os.path.join(os.getcwd(),"parsed_data",doc),'r',encoding='utf-8') as f:
        docData.append(f.read())

it = DocIt.DocIterator(docData,docLabels)

model = gensim.models.Doc2Vec(size = 1000, window=10, min_count =6, workers=11, alpha=0.025, min_alpha=0.01,dm=0,dbow_words=2) #dm=0 for dbow
#model = gensim.models.Doc2Vec(size = 500, window=10, min_count =6, workers=11, alpha=0.025, min_alpha=0.025,dm=1) #initial run
model.build_vocab(it)

model.train(it,total_examples=model.corpus_count,epochs=25)
#initial run
#for epoch in range(20):
#    model.train(it,total_examples=model.corpus_count,epochs=model.iter)
#    model.alpha -= 0.002
#    model.min_alpha = model.alpha
#    model.train(it,total_examples=model.corpus_count,epochs=model.iter)

model.save(os.path.join(doc2vec_dir,"doc2vec.model"))

dictionary = dict()
for val in model.docvecs.offset2doctag:
    dictionary[val]=len(dictionary)

file = open(os.path.join(doc2vec_dir,"dictionary.pkl"),'wb')
pickle._dump(dictionary,file)
file.close()

reverse_dictionary = dict()
for key in dictionary:
    reverse_dictionary[dictionary[key]]=key

file = open(os.path.join(doc2vec_dir,"reverse_dictionary.pkl"),'wb')
pickle._dump(reverse_dictionary,file)
file.close()

'''
temp = {}
reduced = {}
pca = PCA(n_components=300)
#pca = PCA(n_components=100) initial run
for doc in docLabels:
#    temp[doc] = np.reshape(model[doc],(-1,100)) initial run
    temp[doc] = np.reshape(model[doc],(-1,1000))
    reduced[doc] = pca.fit_transform(temp[doc])

np.save(os.path.join(doc2vec_dir,'reduced_dim_vec.npy'),reduced)

#file = open(doc2vec_dir+'\\reduced_dim_vec.pkl','wb')
#pickle._dump(reduced,file)
#file.close()
'''