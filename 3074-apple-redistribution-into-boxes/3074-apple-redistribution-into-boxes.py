class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)

        cum = sum(apple)
        for i,c in enumerate(capacity):
            cum -= c
            if cum <= 0:
                return i+1

        return -1
