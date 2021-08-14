from nltk.tokenize import regexp_tokenize
from nltk.tokenize import RegexpTokenizer

# The RegexpTokenizer class works by compiling your pattern, then calling re.findall() on your text.

# 1
regexp_tokenize("I can't understand you.", "[\w']+")

# 2
tokenizer = RegexpTokenizer("[\w']+")
tokenizer.tokenize("Can't is a contraction.")

whitespace_tokenizer = RegexpTokenizer('\s+', gaps=True)
