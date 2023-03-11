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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        lh = []
        while head:
            lh.append(head.val)
            head = head.next
    
        def makeNode(ll:list) -> TreeNode:
            if not ll: return None       
            idx = int(len(ll) / 2)                
            return TreeNode(ll[idx], makeNode(ll[:idx]), makeNode(ll[idx+1:]))
        
        return makeNode(lh)