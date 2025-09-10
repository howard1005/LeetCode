class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        ans = inf

        l = [set(langs) for langs in languages]

        fl = []

        for a,b in friendships:
            sa,sb = l[a-1],l[b-1]
            if not sa&sb:
                fl.append((a,b))

        for i in range(1,n+1):
            d = defaultdict(set)
            cnt = 0
            for a,b in fl:
                sa,sb = l[a-1],l[b-1]
                if i not in sa and i not in d[a]:
                    cnt += 1
                    d[a].add(i)
                if i not in sb and i not in d[b]:
                    cnt += 1
                    d[b].add(i)
            ans = min(ans,cnt)

        return ans
                