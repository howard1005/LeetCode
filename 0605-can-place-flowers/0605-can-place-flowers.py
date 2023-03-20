class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(flowerbed)):
            flag = 1
            if flowerbed[i] == 1:
                flag = 0
            if i-1>=0 and flowerbed[i-1]==1:
                flag = 0
            if i+1<len(flowerbed) and flowerbed[i+1]==1:
                flag = 0
            if flag:
                flowerbed[i] = 1
                cnt += 1
        return n<=cnt
            