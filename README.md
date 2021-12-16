# job_roles_prediction_models

## Modeling

Model 1: Count Vectorizer + TF-IDF Transformation + Classification Models (onevsrest)

Model 2: Word2Vec Embedding + Classification Models (Random Forest/SGD)

## <strong>I will focus on the following in this post:</strong>

1.Extract features from text using Count Vectorizer and TF-IDF Transformer (equivalent to TF-IDF Vectorizer)

2.Develop Word2vec Embedding and use it in machine learning pipeline

## Extract features using Count Vectorizer — TF-IDF Transformer
Using count vectorizer and TF-IDF transformer is the equivalent of TF-IDF vectorizer. The idea is to first convert a collection of text documents to a matrix of token counts, and then transform a count matrix to a normalized TF (term frequency) or TF-IDF (term frequency–inverse document frequency) representation. When analyzing job descriptions for salary prediction, I realized that it is not easy to find “determining” words only based on counts since all job descriptions are in data fields therefore words like “data”, “analytics” “experiences” have very high frequency. 

## Using Word2Vec Embedding in Classification Models

Word2Vec is a group of related models that are used to produce word embeddings. These models are shallow, one single layer neural networks that are trained to reconstruct linguistic contexts of words.

## 


