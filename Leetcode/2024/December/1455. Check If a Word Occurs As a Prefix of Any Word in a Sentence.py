class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        def isPrefix(x):
            if x[:len(searchWord)] == searchWord:
                return True

        for i in range(len(sentence.split())):
            if isPrefix(sentence.split()[i]):
                return i + 1
        else:
            return -1

# Time complexity: O(N)
# Space complexity: O(1)
s = Solution()
print(s.isPrefixOfWord("i love eating burger", "burg")) # 4