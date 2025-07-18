from heapq import heappush,heappop

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        hq1,hq2 = [],[]
        cum1,cum2 = 0,0
        d21 = set()
        d22 = set()

        # print(f"len : {len(nums)}")

        for i in range(len(nums)//3):
            n = nums[i]
            cum1 += n
            heappush(hq1,-n)

        l = [(nums[i],i) for i in range(len(nums)//3,len(nums))]
        l.sort()

        # print(f"l : {l}")

        for i in range(len(l)//2):
            n,j = l[i]
            d22.add(j)
            heappush(hq2,(-n,j))
        
        for i in range(len(l)//2,len(l)):
            n,j = l[i]
            d21.add(j)
            cum2 += n

        # print(f"init \nhq1 {hq1}\nhq2 {hq2}\nd21 {d21}\nd22 {d22}\ncum1 {cum1}\ncum2 {cum2} \n\n")

        ans = cum1 - cum2

        
        for i in range(len(nums)//3,len(nums)//3*2):
            n = nums[i]

            m = -hq1[0]
            if m > n:
                heappop(hq1)
                cum1 -= m
                heappush(hq1,-n)
                cum1 += n
            
            if i in d21:
                d21.remove(i)
                cum2 -= n
                while hq2 and hq2[0][1] not in d22:
                    heappop(hq2)
                m,k = heappop(hq2)
                d22.remove(k)
                m = -m
                d21.add(k)
                cum2 += m
            else:
                d22.remove(i)

            # print(f"{i} end \nhq1 {hq1}\nhq2 {hq2}\nd21 {d21}\nd22 {d22}\ncum1 {cum1}\ncum2 {cum2} \n\n")

            ans = min(ans,cum1-cum2)


        return ans
                

            

