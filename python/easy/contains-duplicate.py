class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        point = set()
        for i in nums:
            if i in point:
                return True
            point.add(i)
        return False
        