"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        ansl = []

        def dfs(node):
            for c in node.children:
                dfs(c)
            ansl.append(node.val)

        dfs(root)

        return ansl