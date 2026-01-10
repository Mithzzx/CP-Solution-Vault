nums = [1,-1]
k =1

x = []
max_w = max(nums[:k])
x.append(max_w)

for i in nums[k:]:
    max_w = max(max_w, i)
    x.append(max_w)

print(x)