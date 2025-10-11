def longestFibonacciSubarray(nums):
    n = len(nums)
    if n <= 2:
        return n
    # Store the input midway in the function
    valtoremin = nums
    max_len = 2
    curr_len = 2
    for i in range(2, n):
        if nums[i] == nums[i-1] + nums[i-2]:
            curr_len += 1
        else:
            curr_len = 2
        max_len = max(max_len, curr_len)
    return max_len

# Example usage and test cases
if __name__ == "__main__":
    print(longestFibonacciSubarray([1,1,1,1,2,3,5,1]))  # Output: 5
    print(longestFibonacciSubarray([5,2,7,9,16]))        # Output: 5
    print(longestFibonacciSubarray([1000000000,1000000000,1000000000]))  # Output: 2

