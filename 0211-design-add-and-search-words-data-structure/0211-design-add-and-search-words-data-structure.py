class WordDictionary:

    def __init__(self):
        self.root = [0,dict()]

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node[1]:
                node[1][c] = [0,dict()]
            node = node[1][c]
        node[0] = 1
            
    def search(self, word: str) -> bool:
        def dfs(i,node):
            if i == len(word):
                if node[0]:
                    return True
                else:
                    return False
            c = word[i]
            if c == ".":
                for nn in node[1].values():
                    if dfs(i+1,nn): return True
                return False
            elif c in node[1]:
                return dfs(i+1,node[1][c])
            else:
                return False
        return dfs(0,self.root)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)