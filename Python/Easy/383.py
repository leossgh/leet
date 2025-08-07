from collections import Counter
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
class DictSolution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_dict = dict(Counter(magazine))
        try:
            for char in list(ransomNote):
                char_dict[char] -= 1
                if char_dict[char] < 0:
                    return False
            return True
        except:
            return False
class PythonDictSolution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_dict = dict(Counter(magazine))
        try:
            for char in list(ransomNote):
                char_dict[char] -= 1
                if char_dict[char] < 0:
                    return False
            return True
        except:
            return False