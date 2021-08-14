from nltk.corpus import wordnet

syn = wordnet.synsets('person')[0]
lemmas = syn.lemmas()

print(len(lemmas))
print(lemmas[0].name())
print(lemmas[1].name())
print([lemma.name() for lemma in syn.lemmas()])

synonyms = []
for syn in wordnet.synsets('build'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
print(len(set(synonyms)))
print(set(synonyms))
