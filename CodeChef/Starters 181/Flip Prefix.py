# Problem: https://www.codechef.com/problems/FLIPPRE
# Approach: Count the number of flips needed to make the string balanced
# Time Complexity: O(n), Space Complexity: O(1)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    z, o, c = 0, 0, 1

    for i in s:
        if i == "0":
            z += 1
        else:
            o += 1

        if z == o: c += c

    print(c)