# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.res = []
        
        def inorder(root):
            
            if root == None:
                return []
            
            inorder(root.left)
            self.res.append(root)
            inorder(root.right)
        
        inorder(root)
        
        sort = sorted(node.val for node in self.res)
        
        for i in range(len(sort)):
            self.res[i].val = sort[i]
        
        