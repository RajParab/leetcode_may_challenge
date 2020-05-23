"""
Explanation-
-Check if the blocks are aligned properly 
- if yes get the common space in the blocks

"""

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]):
        if A==[] or B==[]:
            return []
        result=[] 
        i=0
        j=0
        while i<len(A) and j<len(B):
            
            if A[i][1]<B[j][0]:
                i+=1
            elif B[j][1]<A[i][0]:
                j+=1
                
            
            else:
                
                ans=[max(A[i][0],B[j][0]),min(A[i][1],B[j][1])]
                result.append(ans)
                if A[i][1]<B[j][1]:
                    i+=1
                else:
                    j+=1
                
        
            
        return result
