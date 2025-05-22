from heapq import heappush,heappop

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        d = defaultdict(list)

        for a,b in queries:
            d[a].append((a,b))

        hq = []

        l = [0 for _ in range((len(nums)))]

        for i,n in enumerate(nums):
            for a,b in d[i]:
                heappush(hq,-b)

            l[i] += l[i-1] if i else 0

            if l[i] >= n:
                continue

            need = n - l[i]

            while need:
                while hq and -hq[0] < i:
                    heappop(hq)

                if not hq:
                    return -1

                b = -heappop(hq)
                
                l[i] += 1
                if b+1 < len(l):
                    l[b+1] -= 1

                need -= 1

        ans = len(hq)

        return ans



            
            
            