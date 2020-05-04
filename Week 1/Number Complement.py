"""
Explaination-
Just need to find 1's complement of the given number
"""

class Solution:
    def findComplement(self, n: int) -> int:
        bits=[]
        answer=0
        while(n!=0):
            bits.append(n%2)
            n=n//2
        for i in range(len(bits)):
            if (bits[i]==0):
                answer+=2**i
        
        return answer