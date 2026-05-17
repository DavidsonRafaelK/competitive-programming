class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 2 != 0 :
            return False
        else:
            return n > 0 and (n & (n - 1)) == 0
