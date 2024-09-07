# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(h,node):
            if h == None:
                return True
            
            nh = h
            if h.val == node.val:
                nh = h.next
            if nh == None:
                return True
            
            ret = False

            if node.left:
                ret |= dfs(nh,node.left)
            if node.right:
                ret |= dfs(nh,node.right)

            return ret

        return dfs(head,root)
            