# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root: TreeNode, k: int,l:List[TreeNode]):
        if(root.left):
            self.traverse(root.left,k,l)
        k-=1
        if k>=0:
            l.append(root)
        else:
            return
        
        if root.right:
            self.traverse(root.right,k,l)
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l=[]
        
        self.traverse(root,k,l)
        
        return l[k-1].val
