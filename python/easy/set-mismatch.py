class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        miss_number = {}
        res = []

        for num in nums:
            if num in miss_number:
                miss_number[num] = miss_number[num] + 1
            else:
                miss_number[num] = 1

        for value in range(1, len(nums) + 1):
            if value not in miss_number:
                res.append(value)
            elif miss_number[value] == 2:
                res.insert(0, value)
        return res