class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_dict = {}
        i=0
        for n in nums:
            if n in target_dict:
                return [target_dict[n],i]
            else:
                target_dict[target-n] = i
            i+=1
class PythonSolution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_dict = {}
        i=0
        for n in nums:
            if n in target_dict:
                return [target_dict[n],i]
            else:
                target_dict[target-n] = i
            i+=1