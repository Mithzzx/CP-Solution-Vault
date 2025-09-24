# https://codeforces.com/problemset/problem/116/A
# Approach: Add the tram's speed to the total speed and find the maximum speed'
# Time Complexity: O(n) Space Complexity: O(1)
# Data Structure: List


arr = []
for _ in range(int(input())):
    x = input().split()
    for j in x : arr.append(int(j))

c = 0
m = 0
for i in range(0,len(arr),2):
    c-= arr[i]
    c+= arr[i+1]
    m = max(m,c)
print(m)