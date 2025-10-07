# Problem: https://codeforces.com/problemset/problem/56/A
# Time Complexity: O(n), Space Complexity: O(1)
# Approach: Count the number of lowercase and uppercase letters and convert the string accordingly
# Data Structure: String

x = input()
lowers = 0
uppers = 0
for i in x:
    if i.islower():
        lowers += 1
    else:
        uppers += 1
if lowers >= uppers:
    print(x.lower())
else:
    print(x.upper())