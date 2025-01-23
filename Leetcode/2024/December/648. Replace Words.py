class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sl = sentence.split(" ")
        for i in dictionary:
            for ind, j in enumerate(sl):
                if i in j[0:len(i)]:
                    sl[ind] = i

        return ' '.join(sl)