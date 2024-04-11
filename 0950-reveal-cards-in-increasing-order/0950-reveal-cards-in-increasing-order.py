class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # 2 3 5 7 11 13 17
        
        def dfs(i):
            if i == len(deck):
                return []
            sl = dfs(i+1)
            rl = [deck[i]]
            if sl:
                rl = [sl[-1]] + rl + sl[:-1]
            return rl
        
        deck.sort()
        return [deck[0]] + dfs(1)
                
                
            