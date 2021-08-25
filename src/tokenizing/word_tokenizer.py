from nltk.tokenize import word_tokenize  # ===
from nltk.tokenize import TreebankWordTokenizer  # 'it', "'s"
from nltk.tokenize import WhitespaceTokenizer  # "it's"
from nltk.tokenize import WordPunctTokenizer  # 'it', "'", 's'

sentence = "The word_tokenize() function is a wrapper function that calls tokenize() on an instance of the TreebankWordTokenizer class. It works by separating words using spaces and punctuation. It doesn't discard the punctuation, allowing you to decide what to do with it."

print(TreebankWordTokenizer().tokenize(sentence))

# The WordPunktTokenizer uses the pattern r'\w+|[^\w\s]+' to tokenize sentences into independent alphabetic and non-alphabetic tokens.

print(WordPunctTokenizer().tokenize(sentence))

# The WhitespaceTokenizer tokenizes sentences into words based on whitespaces like tabs, newlines, and spaces.

print(WhitespaceTokenizer().tokenize(sentence))
