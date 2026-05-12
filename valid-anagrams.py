class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char = {}
        char2 = {}

        for i in s:
            if i in char:
                char[i] = char[i] + 1
            else:
                char[i] = 1
        
        for j in t:
            if j in char2:
                char2[j] = char2[j] + 1
            else:
                char2[j] = 1

        if char == char2:
            return True
        else:
            return False