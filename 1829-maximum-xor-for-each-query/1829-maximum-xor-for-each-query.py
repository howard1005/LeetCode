class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ansl = []
        
        mask = (1<<maximumBit)-1

        x = 0
        for n in nums:
            x ^= n
        
        for n in nums[::-1]:
            k = (x&mask)^mask
            ansl.append(k)
            x ^= n
        
        return ansl