# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dq = deque()
        dq.append(root)
        ans = 0
        while dq:
            node = dq.popleft()
            ans += 1
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        return ans