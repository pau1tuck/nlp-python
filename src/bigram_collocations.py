from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.corpus import stopwords

stopset = set(stopwords.words('english'))
def filter_stops(w): return len(w) < 3 or w in stopset


words = [w.lower() for w in webtext.words('grail.txt')]
bcf = BigramCollocationFinder.from_words(words)
bcf.apply_word_filter(filter_stops)
print(bcf.nbest(BigramAssocMeasures.likelihood_ratio, 4))
