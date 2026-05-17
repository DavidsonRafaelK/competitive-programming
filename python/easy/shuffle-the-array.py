class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []

        for num in range(n):
            res.append(nums[num])
            res.append(nums[num+n])
        
        return res