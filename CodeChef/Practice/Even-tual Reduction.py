# Problem: CodeChef Even-tual Reduction https://www.codechef.com/problems/EVENTUAL
# Time Complexity: O(n), Space Complexity: O(n)
# Approach: Count the frequency of each character and check if the frequency of each character is even or not
# Data Structure: Dictionary

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input())
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for j in d:
        if d[j] % 2 != 0:
            print("NO")
            break
        else:
            print("YES")