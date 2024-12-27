class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        nums.clear()
        for j in [0, 1, 2]:
            if j
            nums.extend([j] * d[j])
