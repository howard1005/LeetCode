class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        ans = 0
        
        vis = {}
        boxq = deque()
        for box in initialBoxes:
            vis[box] = 0
            boxq.append(box)
        
        ksd = set()

        while boxq:
            box = boxq.popleft()

            if box in vis and vis[box] == 1:
                continue
            
            if status[box] or box in ksd:
                for tbox in containedBoxes[box]:
                    if tbox not in vis:
                        vis[tbox] = 0
                        boxq.append(tbox)
                
                for k in keys[box]:
                    ksd.add(k)
                    if k in vis and vis[k] == 0:
                        boxq.append(k)
                
                vis[box] = 1
                ans += candies[box]

        return ans