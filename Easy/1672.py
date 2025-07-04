class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = [0,0]
        for i in range(len(accounts)):
            if sum(accounts[i])>richest[1]:
                richest = [i,sum(accounts[i])]
        return richest[1]
class PythonSolution(object):
    def maximumWealth(accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = [0,0]
        for i in range(len(accounts)):
            if sum(accounts[i])>richest[1]:
                richest = [i,sum(accounts[i])]
        return richest[1]