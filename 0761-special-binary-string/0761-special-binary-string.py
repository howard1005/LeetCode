class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        ans = ''

        # fd,bd = {},{}
        # for i in range(len(s)):
        #     j = i
        #     cnt = 0
        #     while j<len(s):
        #         if s[j] == '1':
        #             cnt += 1
        #         else:
        #             cnt -= 1
        #         if cnt <= 0:
        #             break
        #         j += 1
        #     if cnt == 0 and j<len(s):
        #         fd[j+1] = (i,j)
        #         bd[i] = (i,j)
        # print(fd,bd)

        # print("10"<"1100")
        # print(*(1,2))

        def dec(tl):
            ret = ''
            for i,j in tl:
                ret += s[i:j+1]
            return ret

        def dfs(si,ei):
            # print('dfs',si,ei)
            if si+1 == ei:
                return dec([(si,ei)])

            ret = ''

            l = []
            hi = si
            cnt = 0
            for i in range(si,ei+1):
                if s[i] == '1':
                    cnt += 1
                else:
                    cnt -= 1
                if cnt == 0:
                    l.append((hi,i))
                    hi = i+1
            if len(l) == 1:
                return s[si] + dfs(si+1,ei-1) + s[ei]
            
            ll = []
            for t in l:
                ss = dfs(*t)
                ll.append(ss)
            ll.sort(reverse=True)

            ret = ''.join(ll)
            
            return ret

        ans = dfs(0,len(s)-1)

        return ans