class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        
        sa,sb = set(),set()
        for a,b in zip(A,B):
            sa.add(a)
            sb.add(b)
            ans.append(len(sa&sb))

        return ans