from nltk.stem.snowball import SnowballStemmer
french_stemmer = SnowballStemmer('french', ignore_stopwords=True)

print(french_stemmer.stem('municipalité'))
