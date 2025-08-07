class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #loop through once
        #on a new letter, set a pointer to start counting
        #on a repeat letter, end that counter
        #finish loop with longest length
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        s_chars = list(s)
        pointer_dict = {}
        i = 0
        longest = 0
        #main loop
        for char in s_chars:
            if char in pointer_dict:
                char_len = i-pointer_dict[char]
                first = i-min(pointer_dict.values())
                larger = max(char_len,first)
                if larger > longest:
                    longest = larger
                #pop all keys smaller than dict[char]
                to_pop = [k for k, v in pointer_dict.items() if v <= pointer_dict[char]]
                [pointer_dict.pop(k) for k in to_pop]
            if char not in pointer_dict:
                pointer_dict[char] = i
            i+=1
        val = i-min(pointer_dict.values())
        if val>longest:
            longest = val
        return longest
class PythonSolution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #loop through once
        #on a new letter, set a pointer to start counting
        #on a repeat letter, end that counter
        #finish loop with longest length
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        s_chars = list(s)
        pointer_dict = {}
        i = 0
        longest = 0
        #main loop
        for char in s_chars:
            if char in pointer_dict:
                char_len = i-pointer_dict[char]
                first = i-min(pointer_dict.values())
                larger = max(char_len,first)
                if larger > longest:
                    longest = larger
                #pop all keys smaller than dict[char]
                to_pop = [k for k, v in pointer_dict.items() if v <= pointer_dict[char]]
                [pointer_dict.pop(k) for k in to_pop]
            if char not in pointer_dict:
                pointer_dict[char] = i
            i+=1
        val = i-min(pointer_dict.values())
        if val>longest:
            longest = val
        return longest