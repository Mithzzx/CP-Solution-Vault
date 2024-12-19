class Solution(object):
    def reversePrefix(self, word, ch):
        for ind, i in enumerate(word):
            if i == ch:
                return word[-(len(word) - ind)::-1] + word[ind + 1:]
        return null