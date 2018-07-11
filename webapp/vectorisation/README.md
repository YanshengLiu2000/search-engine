Place parsers.py scraper.py and preprocess.py in a folder.
Run parsers.py and it will ask you to enter the fully qualified pathname of the HTML files.
Enter that wait for it to complete.

I have attached a copy of the scraped and parsed documents in the downloads folder - "Document_Similarity.zip"
--The above mentioned document was unable o be uploaded. I will be uploading it on google drive.

doc2vec uses the doc2vec module to create the word embedding for the documents.
Just run doc2vec.py and it will begin the process of training and creating the vector and also performs a PCA dimensionality reduction
on embeddings.

You need to pass query string or the query filename to get_query_vec(query) of query.py. It returns the PCA reduced vector 
representation of the query.