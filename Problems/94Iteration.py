# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur = root
        s = []
        while True:
            if cur:
                s.append(cur)
                cur = cur.left
            elif s:
                top = s.pop()
                ans.append(top.val)
                cur = top.right
            else: 
                break
        return ans
