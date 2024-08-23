class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """ 
        Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
        
        """
        if n <= 0:
            return False
        elif n==1:
            return True
        else:
            return n%4 == 0 and self.isPowerOfFour(n/4)
        return False
