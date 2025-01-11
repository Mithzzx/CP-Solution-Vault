from collections import defaultdict, Counter

nums = [1,1,1,2,2,3,4,4,4,4]
k = 2
x=[]
count = Counter(nums)
print(count.most_common(3))
print( [item for item, freq in count.most_common(k)])