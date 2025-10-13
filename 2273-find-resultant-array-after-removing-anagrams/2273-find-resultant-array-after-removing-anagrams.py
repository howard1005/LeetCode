class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        def valid(s1,s2):
            l1,l2 = list(s1),list(s2)
            l1.sort()
            l2.sort()
            return l1==l2
            
        st = []
        for w in words:
            if st and valid(w,st[-1]):
                continue
            st.append(w)

        return st
                    