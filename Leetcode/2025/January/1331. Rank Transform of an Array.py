class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        b = sorted(set(arr))

        rank_map = {val: rank for rank, val in enumerate(b, 1)}

        return [rank_map[val] for val in arr]

