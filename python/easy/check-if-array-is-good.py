class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_num = max(nums)
        base = list(range(1, max_num + 1))
        base.append(max_num)
        if sorted(nums) == base:
            return True
        else:
            return False