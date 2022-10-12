# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
            
            def helper(root, s, v):
                
                if root == None:
                    return res
                
                s.append(str(root.val))
                
                if not root.left and not root.right:
                    v.append("->".join(s))
                    
                helper(root.left, s, v)
                helper(root.right, s, v)
                
                s.pop()
                
            res = []
            helper(root, [], res)
            return res