# Solution: https://www.codechef.com/viewsolution/1152529542
# Approach: Use a stack to store the characters of the string and pop the top element if it is equal to the current element
# Time Complexity: O(n), Space Complexity: O(n)

def c(s):
    if s == "":return False
    for i in s:
        if ord(i) in range(97, 123) or ord(i) in range(48, 58):
            continue
        else: return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    end = -1
    for i in s[::-1]:
        if i != " ": break
        else: end -=1
    if s[:2] == "</" and c(s[2:end]) and s[end] == ">":
        print("Success")
    else:
        print("Error")