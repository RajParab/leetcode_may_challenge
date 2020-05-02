#Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/
'''
In this question we need to minimize the number to API calls. We can use binary search for finding first version as it is similar to finding
key in the array. 
'''
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        
        right=n
        left=1
        while(left<right):
            mid = int(left + (right-left)/2)
            if(isBadVersion(mid)):
                right = mid
            else:
                left = mid + 1
        return int(left)