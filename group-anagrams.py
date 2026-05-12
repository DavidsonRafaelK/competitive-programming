class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            if tuple(sorted(word)) not in result:
                result[tuple(sorted(word))] = []
            result[tuple(sorted(word))].append(word)
        return list(result.values())