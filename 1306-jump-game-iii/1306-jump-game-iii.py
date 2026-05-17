class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        vis = [0 for _ in range(len(arr))]
        vis[start] = 1
        q = [start]
        while q:
            i = q.pop()
            if arr[i] == 0:
                return True
            l,r = i-arr[i],i+arr[i]
            if l>=0 and l<len(arr) and vis[l]==0:
                if arr[l] == 0:
                    return True
                vis[l] = 1
                q.append(l)
            if r>=0 and r<len(arr) and vis[r]==0:
                if arr[r] == 0:
                    return True
                vis[r] = 1
                q.append(r)
        return False