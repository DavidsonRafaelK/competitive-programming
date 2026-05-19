class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        same_number = set(nums1) & set(nums2)
        if not same_number: return - 1
        return int(min(same_number))