# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur = root
        s = []
        while True:
            if cur:
                ans.append(cur.val)
                s.append(cur)
                cur = cur.left    
            elif s:
                top = s.pop()
                cur = top.right
            else:
                break         
        return ans
