class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        ml = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def conv(date):
            a,b = date.split('-')
            m,d = int(a),int(b)
            for i in range(m-1):
                d += ml[i]
            return d

        a,b,c,d = conv(arriveAlice),conv(leaveAlice),conv(arriveBob),conv(leaveBob)
        
        i,j = max(a,c),min(b,d)

        ans = 0

        if i<=j:
            ans = j-i+1

        return ans