#Problem Link: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
'''
-------------------QUICK EXPLANATION------------------------------------
Count the apperance of each character string J in string S
'''

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter=0
        for i in J:
            counter+=S.count(i)
        return counter