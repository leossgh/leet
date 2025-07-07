class Solution(object):
    #Misread and solved for mean
    #Mean beats 2058 / 2096 testcases
    def MemoryfindMeanSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = 0
        count = 0
        longer = max(len(nums1),len(nums2))
        new_arr = []
        for i in range(longer):
            try:
                total += nums1[i]
                count +=1
            except:
                print("list empty")
            try:
                total += nums2[i]
                count +=1
            except:
                print("list empty")
        mean = float(total)/float(count)
        #find min which is bigger than mean from both arrs
        #find max which is smaller than mean from both arrs

class Solution(object):
    def MemoryfindMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len = len(nums1)+len(nums2)
        new_arr = []
        for i in range(total_len/2+1):
            if not nums1:
                new_arr.append(nums2[0])
                nums2.pop(0)
            elif not nums2:
                new_arr.append(nums1[0])
                nums1.pop(0)
            else:
                if nums1[0]<nums2[0]:
                    new_arr.append(nums1[0])
                    nums1.pop(0)
                else:
                    new_arr.append(nums2[0])
                    nums2.pop(0)
        if total_len%2==0:
            med = float((new_arr[-2]+ new_arr[-1]))/2
        else:
            med = new_arr[-1]
        return med


        #find min which is bigger than mean from both arrs
        #find max which is smaller than mean from both arrs