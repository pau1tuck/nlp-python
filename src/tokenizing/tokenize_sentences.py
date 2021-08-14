from nltk.tokenize import BlanklineTokenizer
from nltk.tokenize import sent_tokenize
# ===
import nltk.data
sentence_tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')

paragraph = "If you look up ‘tea’ in the first cookery book that comes to hand you will probably find that it is unmentioned; or at most you will find a few lines of sketchy instructions which give no ruling on several of the most important points. This is curious, not only because tea is one of the mainstays of civilization in this country, as well as in Eire, Australia and New Zealand, but because the best manner of making it is the subject of violent disputes. When I look through my own recipe for the perfect cup of tea, I find no fewer than 11 outstanding points. On perhaps two of them there would be pretty general agreement, but at least four others are acutely controversial."

sentences_1 = sent_tokenize(paragraph)
sentences_2 = sentence_tokenizer.tokenize(paragraph)

for sentence in sentences_2:
    print(sentence)
