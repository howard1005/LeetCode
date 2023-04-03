class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        i,j = 0,len(people)-1
        while i<=j:
            ans += 1
            remain = limit-people[j]
            j-=1
            if remain >= people[i]:
                i+=1
        return ans