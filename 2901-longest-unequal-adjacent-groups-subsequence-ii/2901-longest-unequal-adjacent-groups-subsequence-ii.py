class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []

        d = defaultdict(set)

        for i,w in enumerate(words):
            size = len(w)
            for j in range(size):
                nw = w[:j] + '?' + (w[j+1:] if j+1<size else '')
                d[(size,nw)].add(i)

        # print(d)

        ed = defaultdict(set)
        inds = defaultdict(int)

        for i,w in enumerate(words):
            size = len(w)
            sl = set()
            for j in range(size):
                nw = w[:j] + '?' + (w[j+1:] if j+1<size else '')
                sl |= d[(size,nw)]
            for j in sl:
                if i >= j:
                    continue
                if groups[i] == groups[j]:
                    continue
                ed[i].add(j)
                inds[j] += 1

        # print(ed)

        vis = defaultdict(list)
        ians = []

        def tro(i):
            nonlocal ians
            dq = deque()
            vis[i] = [i]
            dq.append(i)
            while dq:
                i = dq.popleft()
                for j in ed[i]:
                    inds[j] -= 1
                    if len(vis[j]) < len(vis[i])+1:
                        vis[j] = vis[i] + [j]
                    if inds[j] == 0:
                        dq.append(j)

        for i in range(len(words)):
            if i in vis:
                continue
            tro(i)

        for l in vis.values():
            if len(ians) < len(l):
                ians = l
            
        ans = [words[i] for i in ians]

        return ans