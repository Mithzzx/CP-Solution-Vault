# Problem: Trapping Rain Water
# Difficulty: Hard
# approach: use two pointers to find the maximum height from left and right, then calculate the water trapped
# Time complexity: O(n), Space complexity: O(1)

height = [0,1,0,2,1,0,1,3,2,1,2,1]
l, r = 0, len(height) - 1
left_max, right_max  = height[l], height[r]
water = 0

while l < r:
    if left_max < right_max:
        l += 1
        left_max = max(left_max, height[l])
        water += left_max - height[l]
    else:
        r -= 1
        right_max = max(right_max, height[r])
        water += right_max - height[r]

print(water)