from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

print(stemmer.stem('excreting'))
print(stemmer.stem('excretion'))
