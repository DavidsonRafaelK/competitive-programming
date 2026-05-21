class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        nums1 = list(map(str, arr1))
        nums2 = list(map(str, arr2))

        mx_pref = 0
        sv = set()

        for num in nums1:
            for i in range(1, len(num) + 1):
                sv.add(num[0:i])

        for num2 in nums2:
            for i in range(1, len(num2) + 1):
                if num2[0:i] in sv:
                    mx_pref = max(mx_pref, i)

        return mx_pref
