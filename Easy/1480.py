class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = []
        for i in range(len(nums)):
            if i == 0:
                sums.append(nums[i])
            else:
                sums.append(sums[i-1]+nums[i])
        return sums