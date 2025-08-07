class MemorySolution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = list(s)
        sum=0
        i = 0
        while i<len(arr):
            curr = arr[i]
            try:
                next = arr[i+1]
            except:
                next=""
            if curr == "I":
                if next=="V":
                    sum+=4
                    i+=1
                elif next == "X":
                    sum+=9
                    i+=1
                else:
                    sum+=1
            elif curr == "X":
                if next=="L":
                    sum+=40
                    i+=1
                elif next == "C":
                    sum+=90
                    i+=1
                else:
                    sum+=10
            elif curr == "C":
                if next=="D":
                    sum+=400
                    i+=1
                elif next == "M":
                    sum+=900
                    i+=1
                else:
                    sum+=100
            elif curr == "V":
                sum+=5
            elif curr == "L":
                sum+=50
            elif curr == "D":
                sum+=500
            elif curr == "M":        
                sum+=1000
            else:
                print('unknown error')
            i+=1
        return sum
class TimeSolution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[s[i]]
            else:
                result += roman_to_int[s[i]]
        return result