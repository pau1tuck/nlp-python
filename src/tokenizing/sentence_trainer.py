from nltk.tokenize import PunktSentenceTokenizer
# NLTK corpus method:
from nltk.corpus import webtext
text = webtext.raw('overheard.txt')

# Direct method:
with open('/usr/share/nltk_data/corpora/webtext/overheard.txt', encoding='ISO-8859-2') as f:
    text = f.read()

# p.15
# The PunktSentenceTokenizer class uses an unsupervised learning algorithm to learn what constitutes a sentence break.
# It is unsupervised because you don't have to give it any labeled training data, just raw text.

# Trainer:
sentence_tokenizer = PunktSentenceTokenizer(text)

sentences = sentence_tokenizer.tokenize(text)
print(sentences[0:60])

# The specific technique used in this case is called sentence boundary detection and it works by counting punctuation and tokens that commonly end a sentence, such as a period or newline, then using the resulting frequencies to decide what the sentence boundaries should actually look like.
