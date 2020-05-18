"""
Explanation -
Compare the sorted s1 with sliced and sorted s2
"""



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        s1_list=sorted(s1)
        s1_len=len(s1)
        for i in range(len(s2)):
            s2_block=sorted(s2[i:i+s1_len])
            if s2_block==s1_list:
                return True
            
        return False
