
def smallest_subarray_sum(nums, target):
    current_sum = 0
    start = 0
    min_length = float('inf')
    min_subarray = []

    for end in range(len(nums)):
        current_sum += nums[end]

        while current_sum >= target:
            if current_sum == target and (end - start + 1) < min_length:
                min_length = end - start + 1
                min_subarray = nums[start:end + 1]
            current_sum -= nums[start]
            start += 1
            
    if min_subarray == []:
        return [-1]
    return min_subarray

# Example usage:
nums = [6,3,5,2]
p = 5

target = sum(nums) % p
if target == 0:
    print(0)
print(smallest_subarray_sum(nums, target))
print(len(smallest_subarray_sum(nums, target)))  # Output: [2, 3, 4]