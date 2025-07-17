class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        el_sum = 0
        digit_sum = 0
        for num in nums:
            el_sum += num
            chars = [int(c) for c in list(str(num))]
            for n in chars:
                digit_sum += n
            print(chars)
        return abs(el_sum-digit_sum)