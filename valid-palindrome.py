class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        if s[::-1] == s:
            return True
        else:
            return False

# Atau

s = s.lower().replace(" ", "").replace("?", "").replace(",", "").replace("'", "").replace("!", "").replace(".", "").replace(":", "")
    if s[::-1] == s:
        return True
    else:
        return False