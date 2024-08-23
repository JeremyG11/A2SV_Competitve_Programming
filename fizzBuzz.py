class FuzzBizz(object):
    """
    Write a program that outputs the string representation of numbers from 1 to n.
    But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
    """
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        
        """
        result = []
        for i in range(1,n+1):
            
            if(i %3==0 and i % 5 == 0):
                result.append("FizzBuzz")
            elif(i % 3 == 0):
                result.append("Fizz")
            elif(i % 5 == 0):
                result.append("Buzz")
            else:
                 result.append(str(i)) 
        return result
