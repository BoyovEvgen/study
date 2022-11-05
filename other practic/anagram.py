def anagrams(word, words):
    wrd = sorted(word)
    return [w for w in words if sorted(w) == wrd]


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))