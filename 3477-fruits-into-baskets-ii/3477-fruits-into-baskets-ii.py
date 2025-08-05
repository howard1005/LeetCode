class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        
        vis = set()

        for f in fruits:
            mat = False
            for i,b in enumerate(baskets):
                if i not in vis and f<=b:
                    vis.add(i)
                    mat = True
                    break
            if not mat:
                ans += 1
        
        return ans
                