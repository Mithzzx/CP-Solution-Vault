class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        B = []
        for i in range(len(nums) + 1):
            for j in range(i + 1, len(nums) + 1):
                sub = nums[i:j]
                B.append(sum(sub))
        B.sort()
        print(sum(B[left - 1:right]))
