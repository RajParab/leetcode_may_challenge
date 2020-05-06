"""
Explaination-
Take count of all elements in the list,
Return the first number from the most_common list
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        c=Counter(nums)
        return c.most_common()[0][0]