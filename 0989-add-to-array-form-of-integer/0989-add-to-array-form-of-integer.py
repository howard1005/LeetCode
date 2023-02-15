class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:        
        return map(lambda c: int(c), list(str(int(''.join(map(lambda c: str(c), num)))+k)))