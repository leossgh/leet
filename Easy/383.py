class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_list = list(magazine)
        try:
            for char in list(ransomNote):
                mag_list.remove(char)
            return True
        except:
            return False
class PythonSolution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_list = list(magazine)
        try:
            for char in list(ransomNote):
                mag_list.remove(char)
            return True
        except:
            return False