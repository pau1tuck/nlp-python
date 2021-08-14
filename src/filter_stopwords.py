from nltk.corpus import stopwords

english_stopwords = set(stopwords.words('english'))

words = ["Can't", 'is', 'a', 'contraction']

print([word for word in words if word not in english_stopwords])
