class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                arr.append("FizzBuzz")
            elif i%3 == 0:
                arr.append("Fizz")
            elif i%5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(i))
        return arr
    
    def scalable_fizz_buzz(n):
        arr = []
        for i in range(1,n+1):
            current_string = ""
            if i%3 == 0:
                current_string += "Fizz"
            if i%5 == 0:
                current_string += "Buzz"
            if current_string == "":
                arr.append(i)
            else:
                arr.append(current_string)
        return arr
#print(Solution.scalable_fizz_buzz(15))