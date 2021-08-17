from nltk.stem import RegexpStemmer
stemmer = RegexpStemmer('ing')

print(stemmer.stem('cooking'))
print(stemmer.stem('cookery'))
print(stemmer.stem('ingleside'))
