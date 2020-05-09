"""
Explaination - 
Approach 1 - Check each number till you reach the answerr

Approach 2 - Find the answer by raising to 0.5 to the number is a integer type

"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        Approach 1 -
        if num < 2 or num==4:
            return True
        elif num == 2 or num==3:
            return False
        num_digits=len(str(num))
        power_of_answer=((num_digits//2)+1)
        for i in range(2,10**power_of_answer):
            if num%i==0:
                ans=num//i
                if ans==num//i and i==ans:
                    print(ans,i)
                    return True
                print(ans,i)
        return False"""
        
        
        # Approach 2
        if num**0.5==int(num**0.5):
            return True
        else:
            return False
