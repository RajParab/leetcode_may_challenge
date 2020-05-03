"""
Explaination-

-count the different characters in Magazine and store in dictionary
-return False if character in ransomNote doesn't exist in dictionary 
or the count of character in ransomNote is greater than magazine

"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_set=set(magazine)
        ransomNote_set=set(ransomNote)
        magazine_dict={}
        for i in magazine_set:
            magazine_dict[i]=magazine.count(i)
        for i in ransomNote_set:
            if i not in magazine_dict:
                return False
            elif ransomNote.count(i)>magazine_dict[i]:
                return False
        
        return True