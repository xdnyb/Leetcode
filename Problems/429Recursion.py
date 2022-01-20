"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        def helper(node, level):
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)
            for child in node.children:
                helper(child, level+1)
        
        ans = []
        if root:
            helper(root, 0)
        return ans
