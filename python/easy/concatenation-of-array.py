class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans.extend(nums * 2)

        return ans