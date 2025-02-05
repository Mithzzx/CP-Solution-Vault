# Problem: 2206. Divide Array Into Equal Pairs
# Difficulty: Easy
# approach: use set to store the elements, if the element is already in the set, remove it, else add it. If the set is empty, return True, else False
# Time complexity: O(n), Space complexity: O(n)



nums = [3,2,3,2,2,2]

d = set()
for i in nums:
    d.remove(i) if i in d else d.add(i)
print(False if d else True)