class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        #find gaps
        #gaps = []
        gap_lengths = []
        i=0
        while i<len(startTime):
            if i is 0:
        #        gaps.append([0,startTime[i]])
                gap_lengths.append(startTime[i]-0)
                i+=1
        #    gaps.append([endTime[i-1],startTime[i]])
            gap_lengths.append(startTime[i]-endTime[i-1])
            i+=1
        #gaps.append([endTime[i-1],eventTime])
        gap_lengths.append(eventTime-endTime[i-1])
            #if i in startTime:
                #gaps.append([i,i])
            #    i=endTime[j]
            #    j+=1
            #else:
            #    if j<=len(startTime)-1:
            #        gaps.append([i,startTime[j]])
            #        i = startTime[j]
            #    else:
            #        gaps.append([endTime[j-1],eventTime])
            #        break
        if not gap_lengths:
            return 0
        if len(gap_lengths) is 1:
            return max(gap_lengths)
        #if len(gap_lengths)<=k:
        #    return 0
        #longest_k_gap_len = 0
        #for i in range(len(gaps)-k):
        #    gap_lengths = [b - a for a, b in gaps]
            #result = sum(gap_lengths[i:i + k + 1])
        #    if result>longest_k_gap_len:
        #        longest_k_gap_len = result
        #gap_lengths = [b - a for a, b in gaps]
        if len(gap_lengths) < k + 1:
            return sum(gap_lengths)  

        window_sum = sum(gap_lengths[:k + 1])
        max_sum = window_sum

        for i in range(1, len(gap_lengths) - k):
            window_sum = window_sum - gap_lengths[i - 1] + gap_lengths[i + k]
            max_sum = max(max_sum, window_sum)
        return max_sum