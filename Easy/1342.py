class PythonRecursiveSolution(object):
    def recursive(self,num,steps):
        print(steps)
        if num > 0:
            if num%2==0:
                steps = self.recursive(PythonRecursiveSolution,num/2,steps+1)
            else:
                steps = self.recursive(PythonRecursiveSolution,num-1,steps+1)
        return steps

    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.recursive(PythonRecursiveSolution,num,0)

class PythonSolution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            if num%2 == 0:
                num /= 2
                steps+=1
            else:
                num -= 1
                steps += 1
        return steps
    
class PythonBitwiseSolution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            if (num&1)==0:
                num >>= 1
                steps+=1
            else:
                num -= 1
                steps += 1
        return steps
    
class RecursiveSolution(object):
    def recursive(self,num,steps):
        print(steps)
        if num > 0:
            if num%2==0:
                steps = self.recursive(num/2,steps+1)
            else:
                steps = self.recursive(num-1,steps+1)
        return steps

    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.recursive(num,0)

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            if num%2 == 0:
                num /= 2
                steps+=1
            else:
                num -= 1
                steps += 1
        return steps
    
class BitwiseSolution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0:
            if (num&1)==0:
                num >>= 1
                steps+=1
            else:
                num -= 1
                steps += 1
        return steps