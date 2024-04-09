class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        
        while 1:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    ans += 1
                if i == k and tickets[i] == 0:
                    return ans
        
        return ans