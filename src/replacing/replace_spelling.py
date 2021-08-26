import enchant
from replacers import SpellingReplacer
replacer = SpellingReplacer()

print(replacer.replace('cookbok'))

# The SpellingReplacer class starts by creating a reference to an Enchant dictionary. Then, in the replace() method, it first checks whether the given word is present in the dictionary. If it is, no spelling correction is necessary and the word is returned. If the word is not found, it looks up a list of suggestions and returns the first suggestion, as long as its edit distance is less than or equal to max_dist. The edit distance is the number of character changes necessary to transform the given word into the suggested word. The max_dist value then acts as a constraint on the Enchant suggest function to ensure that no unlikely replacement words are returned.

dictionary = enchant.Dict('en')
print(dictionary.suggest('languege')[:5])
