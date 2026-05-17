class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        max_counter = 0

        for num in nums:
            if  num != 1:
                curr = 0
            else:
                curr += 1
                max_counter = max(max_counter, curr)
                
        return max_counter            
