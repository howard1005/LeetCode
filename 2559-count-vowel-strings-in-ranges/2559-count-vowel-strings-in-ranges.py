class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vs = ('a','e','i','o','u')
        def valid(w):
            if w[0] in vs and w[-1] in vs:
                return True
            return False
        
        l = [0 for _ in range(len(words))]

        for i,w in enumerate(words):
            l[i] = l[i-1] if i else 0
            if valid(w):
                l[i] += 1

        def get(i,j):
            return l[j]-(l[i-1] if i else 0)


        ans = []

        for a,b in queries:
            ans.append(get(a,b))

        return ans