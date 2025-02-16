from collections import defaultdict

s1 = "ab"
s2 = "ab"
l,r,freq = 0,len(s1)-1,defaultdict(int)
s1dict = defaultdict(int)
for i in s1:
    s1dict[i] += 1
for j in s2[:r+1]:
    freq[j] += 1

while r < len(s2)-1:
    if freq == s1dict:
        print(True)
        break

    l += 1
    r += 1

    freq[s2[r]] += 1
    freq[s2[l-1]] -= 1
    if freq[s2[l-1]] == 0:
        del freq[s2[l-1]]


else:
    print(False)