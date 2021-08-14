from nltk.corpus import wordnet

syn = wordnet.synsets('dog')[0]

print(syn.name())
print(syn.pos())
print(syn.definition())
print(syn.examples())
print(syn.hypernyms())
print(syn.hypernyms()[0].hyponyms())
print(syn.hypernym_paths())
