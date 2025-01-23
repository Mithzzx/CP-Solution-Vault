from collections import defaultdict

strs = ["","",""]

anagram_map = defaultdict(list)
for word in strs:
    sorted_word = ''.join(sorted(word))
    anagram_map[sorted_word].append(word)
print(list(anagram_map.values()))  # Output: [['', ''], ['']]