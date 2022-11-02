# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        
        if root.left == None:
            return root.right
        
        if root.right == None:
            return root.left
        
        if root.left and root.right:
            temp = root.right
            
            while temp.left:
                temp = temp.left
            
            root.val = temp.val
            root.right = self.deleteNode(root.right, root.val)
        
        return root