class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n==1:
            return True
        else:
            return n%4 == 0 and self.isPowerOfFour(n/4)
        return False
