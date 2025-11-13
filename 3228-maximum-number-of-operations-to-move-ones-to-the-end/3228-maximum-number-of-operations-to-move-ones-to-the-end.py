class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0

        l = s.split('0')
        # print(l)
        cuml = []
        for s in l:
            cnt = len(s)
            if cnt:
                cuml.append(cnt)
        # print(cuml)
        for i in range(1,len(cuml)):
            cuml[i] += cuml[i-1]

        
        # print(cuml)
            
        ans = sum(cuml[:-1])

        return ans