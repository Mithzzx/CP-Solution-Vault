s = "aab"


def isPalindrome(x):
    if x == x[::-1]:
        out.append(x)


out = []

length = len(s) + 1
lp = 0
rp = 0

while lp < length:
    rp = lp + 1
    while rp < length:
        isPalindrome(s[lp:rp])
        rp += 1
    lp += 1

print(out)
