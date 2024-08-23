import math
class Solution:
    """ 
    Given an integer (signed 32 bits), write a function to check whether it is a power of 3.
    """
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n==1:
            return True
        else:
            return n%3 == 0 and self.isPowerOfThree(n/3)
        return False
