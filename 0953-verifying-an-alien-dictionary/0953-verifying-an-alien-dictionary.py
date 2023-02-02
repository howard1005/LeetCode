class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c1:c2 for c1,c2 in zip(order,'abcdefghijklmnopqrstuvwxyz')}
        def conv(s):
            return ''.join([d[c] for c in s])
        return words == list(sorted(words, key=lambda x:conv(x)))