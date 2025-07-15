class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        last_word = words[-1]
        return len(list(last_word))
    #3