"""
Explanation-
Get the existing color stored in the given pixel
Apply floodfill to all the adjacent points with the given colour

"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if len(image)==0:
            return image
        prevC=image[sr][sc]
        def floodFill(sr,sc):
            
            
            if sr<0 or sc<0 or sr>=len(image) or sc>=len(image[0]) or image[sr][sc]!=prevC or image[sr][sc]==newColor:
                return 

            image[sr][sc]=newColor
            
            floodFill(sr,sc-1)
            floodFill(sr,sc+1)
            floodFill(sr-1,sc)
            floodFill(sr+1,sc)

            
        floodFill(sr,sc)
        
        return image
