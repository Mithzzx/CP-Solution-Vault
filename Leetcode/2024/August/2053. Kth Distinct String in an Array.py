class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print(d)
        t = []
        for key in d:
            if d[key] == 1:
                t.append(key)
        print(len(t))
        if k - 1 in range(len(t)):
            print(t[k - 1])
        else:
            print("")
