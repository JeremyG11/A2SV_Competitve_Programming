import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n==1:
            return True
        else:
            return n%3 == 0 and self.isPowerOfThree(n/3)
        return False
