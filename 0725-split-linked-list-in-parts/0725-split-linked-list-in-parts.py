# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ansl =[[] for _ in range(k)]
        sizes =[0 for _ in range(k)]
        nl = []
        h = head
        while h:
            nl.append(h)
            h=h.next
        
        for i in range(len(nl)%k):
            sizes[i]+=1
        for i in range(len(sizes)):
             sizes[i]+=len(nl)//k
        ofs=0
        for i,size in enumerate(sizes):
            ansl[i].extend(nl[ofs:ofs+size])
            ofs+=size
        
        for l in ansl:
            if l:
                l[-1].next=None
        ans = [l[0] if l else None for l in ansl]
        return [l[0] if l else None for l in ansl]
        