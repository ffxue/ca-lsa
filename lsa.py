from __future__ import print_function
from gensim.models import KeyedVectors
from nltk.corpus import stopwords
import nltk
import time

# fasttext_file = 'PATH__TO__fasttext_vector_file'
fasttext_file = 'C:/wiki/wiki-news-300d-1M.vec'
# keyword file
keyword_file = 'txt/cat-20180630.txt'
# document file
document_file = 'txt/docs-20180703.txt'

# max_similarity between a keyword and a sentence (document)
def lsa(sentence, keyword):
    ret = 0
    for word in sentence:
        try:
            result = en_model.n_similarity(keyword, [word])
            ret = max(ret, result);
        except:
            pass
    return ret

# max_similarity between a set of keywords ("; "-seperated) and a sentence (document)
def lsa_category(sentence, keywords):
    ret = 0
    for term in keywords:
        try:
            keyword = [w.strip() for w in term.lower().split()]
            if (len(keyword) > 0):
                result = lsa(sentence, keyword)
                ret = max(ret, result);
#                print(keyword)
#                print(result)
        except:
            pass
    return round(ret,4)


# Creating the model
en_model = KeyedVectors.load_word2vec_format(fasttext_file)

print('Loading Facebook fasttext ... (This may require a couple of minutes)')
# load keys and prepare key words
with open(keyword_file, mode='r', encoding='utf-8') as f:
    txtkeys5 = f.readlines()

category = []
for line in txtkeys5:
    phrases = [w.strip() for w in line.lower().split(';')]
    category.append(phrases)

# load documents/texts
with open(document_file, mode='r', encoding='utf-8') as f:
    docs = f.readlines()

# load stopwords 
stopwords = nltk.corpus.stopwords.words('english')

start_time = time.time()

# loop for each document (lines)
for i in range(0,len(docs)):
    res = []
    # loop for each category (column)
    for cat in category:
        # split sentence to words
        s = [w.strip() for w in docs[i].lower().split() if w not in stopwords]
        # compute lsa
        lsa_similarity = lsa_category(s, cat)
        res.append(lsa_similarity)
    
    print(res)

elapsed_time = time.time() - start_time

print('Total time: ' + str(elapsed_time)+ 's')
