# Problem: https://codeforces.com/problemset/problem/218/A
# Time Complexity: O(n), Space Complexity: O(1)
# Approach: Convert the first character to uppercase if it is lowercase
# Data Structure: String

x = input()
if ord(x[0]) < 97 or ord(x[0]) > 122:
    print(x)
else:
    print(chr(ord(x[0])-32)+x[1:])