class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        def proc(lead):
            ret = []

            for w,g in zip(words,groups):
                if g == lead:
                    ret.append(w)
                    lead ^= 1
            
            return ret

        ans = None

        l1,l2 = proc(0),proc(1)
        if len(l1) < len(l2):
            ans = l2
        else:
            ans = l1

        return ans
            
            