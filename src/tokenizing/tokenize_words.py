from nltk.tokenize import word_tokenize
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import WordPunctTokenizer

sentence = "All true tea lovers not only like their tea strong, but like it a little stronger with each year that passes — a fact that's recognized in the extra ration issued to old-age pensioners."

print(WhitespaceTokenizer().tokenize(sentence))
