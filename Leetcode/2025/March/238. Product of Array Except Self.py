# Problem: 238. Product of Array Except Self
# Difficulty: Medium
# approach: use two pointers to store the prefix and postfix product of the array, then multiply them to get the result
# Time complexity: O(n), Space complexity: O(1)

nums = [-1,1,0,-3,3]
x = [1]*len(nums)

prefix ,postfix = 1,1
for ind, i in enumerate(nums):
    x[ind] = prefix if ind > 0 else 1
    prefix *= i

for j in range(1,len(nums)+1):
    x[-j] *= postfix
    postfix *= nums[-j]

print(x)