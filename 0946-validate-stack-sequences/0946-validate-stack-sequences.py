class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        i,j = 0,0
        while 1:
            if j<len(popped) and st and st[-1] == popped[j]:
                st.pop()
                j+=1
            elif i<len(pushed):
                st.append(pushed[i])
                i+=1
            else:
                break
        if i==len(pushed) and j==len(popped):
            return True
        return False