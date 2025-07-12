class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:

        ansd = set()
        
        def getij(l):
            i = len(l)//2 -(1 if len(l)%2 == 0 else 0)
            j = len(l) - 1 - i
            return i,j
        
        def valid(l):
            i,j = getij(l)
            while i>=0:
                if (l[i],l[j]) == (firstPlayer,secondPlayer):
                    return True
                i -= 1
                j += 1
            return False

        def dfs(i,j,l,dq,ll):
            if i < 0:
                ll.add(tuple(dq))
                return 

            if i == j:
                dq.append(l[j])
                dfs(i-1,j+1,l,dq,ll)
                dq.pop()
                return
            
            if l[j] not in (firstPlayer,secondPlayer):
                dq.appendleft(l[i])
                dfs(i-1,j+1,l,dq,ll)
                dq.popleft()

            if l[i] not in (firstPlayer,secondPlayer):
                dq.append(l[j])
                dfs(i-1,j+1,l,dq,ll)
                dq.pop()

        @cache
        def round(r,l):
            if not l:
                return
            if valid(l):
                ansd.add(r)
                return

            i,j = getij(l)
            ll = set()
            dfs(i,j,l,deque(),ll)
            # print(f"\nround {r},{l}")
            # print(f"ll {ll}")

            for l in ll:
                round(r+1,l)

        round(1,tuple(i+1 for i in range(n)))

        # print(ansd)

        ans = (min(ansd),max(ansd))

        return ans

            


        

                
        


        
