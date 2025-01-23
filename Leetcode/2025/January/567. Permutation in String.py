nums = [100,4,200,1,3,2]
nums_set = set(nums)
max_len = 0
for num in nums_set:
    if num-1 not in nums_set:
        current_num = num
        current_len = 1
        while current_num+1 in nums_set:
            current_num += 1
            current_len += 1
        max_len = max(max_len, current_len)
