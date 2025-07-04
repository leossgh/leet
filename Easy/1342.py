class PythonSolution(object):
    def recursive(self,num,steps):
        print(steps)
        if num!=0:
            if num%2==0:
                steps = self.recursive(PythonSolution,num/2,steps+1)
            else:
                steps = self.recursive(PythonSolution,num-1,steps+1)
        return steps

    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.recursive(PythonSolution,num,0)
    
class RecursiveSolution(object):
    def recursive(self,num,steps):
        print(steps)
        if num!=0:
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
        while num != 0:
            if num%2 == 0:
                num = num/2
                steps+=1
            else:
                num -= 1
                steps += 1
        return steps