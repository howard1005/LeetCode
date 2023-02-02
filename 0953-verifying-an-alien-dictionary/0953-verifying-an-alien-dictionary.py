class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c1:c2 for c1,c2 in zip(order,'abcdefghijklmnopqrstuvwxyz')}
        return words == list(sorted(words, key=lambda s:''.join([d[c] for c in s])))