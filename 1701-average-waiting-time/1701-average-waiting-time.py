class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cum = 0
        i = 0
        t = 0
        while i<len(customers):
            a,k = customers[i]
            cum += max(t,a)-a+k 
            t = max(t,a) + k
            i += 1
        
        return cum/len(customers)