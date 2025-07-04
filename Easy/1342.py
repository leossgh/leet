class SolutionPython(object):
    def recursive(self,num,steps):
        print(steps)
        if num!=0:
            if num%2==0:
                steps = self.recursive(SolutionPython,num/2,steps+1)
            else:
                steps = self.recursive(SolutionPython,num-1,steps+1)
        return steps

    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.recursive(SolutionPython,num,0)
    
class Solution(object):
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