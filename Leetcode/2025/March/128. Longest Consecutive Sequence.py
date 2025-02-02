# Problem: 128. Longest Consecutive Sequence
# Difficulty: Medium
# approach: use set to store the elements, iterate through the set, if the element is not in the set, add it to the set and check the length of the consecutive sequence
# Time complexity: O(n), Space complexity: O(n)

nums = [100,4,200,1,3,2]
s = set(nums)
seen=set()
ll=0

for i in nums:
    cl=0
    if i not in seen:
        seen.add(i)
        cl+=1
        low = i-1
        high = i+1
        while low in s:
            cl+=1
            seen.add(low)
            low-=1
        while high in s:
            cl+=1
            seen.add(high)
            high+=1

    ll = max(ll,cl)

print(ll)
