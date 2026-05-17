class Solution:
    def findMin(self, nums: List[int]) -> int:
        index = 0
        high = len(nums) - 1

        while index < high:
            middle = (index + high) // 2
            if nums[middle] > nums[high]:
                index = middle + 1
            else:
                high = middle
        return nums[index]