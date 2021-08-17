from nltk.stem import LancasterStemmer
stemmer = LancasterStemmer()

print(stemmer.stem('excreting'))
print(stemmer.stem('excretion'))
