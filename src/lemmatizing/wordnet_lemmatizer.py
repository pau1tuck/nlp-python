from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

print(lemmatizer.lemmatize('playing', pos='n'))
print(lemmatizer.lemmatize('playing', pos='v'))
print(lemmatizer.lemmatize('players'))

print(stemmer.stem('believes'))
print(lemmatizer.lemmatize('believes', pos='v'))
