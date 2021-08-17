from nltk.corpus import webtext
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures
from nltk.corpus import stopwords

stopset = set(stopwords.words('english'))
def filter_stops(w): return len(w) < 3 or w in stopset


words = [word.lower() for word in webtext.words('singles.txt')]

tcf = TrigramCollocationFinder.from_words(words)

tcf.apply_word_filter(filter_stops)

# remove any trigrams that occurred less than three times:
tcf.apply_freq_filter(3)

print(tcf.nbest(TrigramAssocMeasures.likelihood_ratio, 4))
