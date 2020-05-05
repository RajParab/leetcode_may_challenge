"""
Explanation-
Count the occurrence of each character, if it appears more than once return the index
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i)==1:
                return s.find(i)
        return -1