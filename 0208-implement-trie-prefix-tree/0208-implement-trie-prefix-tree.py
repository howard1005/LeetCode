class Trie:

    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        d = self.d
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['end'] = 1
        
    def search(self, word: str) -> bool:
        d = self.d
        for c in word:
            if c not in d:
                return False
            d = d[c]
        if 'end' in d:
            return True
        return False
            
    def startsWith(self, prefix: str) -> bool:
        d = self.d
        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)