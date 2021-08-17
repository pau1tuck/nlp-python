from nltk.tokenize import regexp_tokenize
from nltk.tokenize import RegexpTokenizer

# The RegexpTokenizer class works by compiling your pattern, then calling re.findall() on your text.

# 1
regexp_tokenize("I can't understand you.", "[\w']+")

# 2
tokenizer = RegexpTokenizer("[\w']+")
tokenizer.tokenize("Can't is a contraction.")

# The gaps parameter, if set to True, is used to find the gaps between the tokens. Otherwise, it is used to find the tokens themselves.
whitespace_tokenizer = RegexpTokenizer(r'\s+', gaps=True)
word_tokenizer = RegexpTokenizer(pattern=r'\w+', gaps=False)

sentence = "The brown fox wasn't that quick and he couldn't win the race."

word_indices = list(whitespace_tokenizer.span_tokenize(sentence))
print(word_indices)
print([sentence[start:end] for start, end in word_indices])
print(word_tokenizer.tokenize(sentence))
