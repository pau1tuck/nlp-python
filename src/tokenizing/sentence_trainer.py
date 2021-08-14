from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext
text = webtext.raw('overheard.txt')

# Trainer:
sentence_tokenizer = PunktSentenceTokenizer(text)

sentences = sentence_tokenizer.tokenize(text)
print(sentences[0:60])
