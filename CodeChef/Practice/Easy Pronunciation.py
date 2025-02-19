# Problem: Easy Pronunciation https://www.codechef.com/problems/EZSPEAK
# Approach: Check if the string contains 4 consecutive consonants
# Time Complexity: O(n), Space Complexity: O(1)
# Data Structure: Set

t = int(input())
for _ in range(t):
    n = input()
    s = input()
    count = 0
    vowels = {"a", 'e','i', 'o', 'u'}
    for i in s:
        if i in vowels:
            count = 0
            continue
        count+=1
        if count == 4:
            print("NO" )
            break
    else:
        print("YES")