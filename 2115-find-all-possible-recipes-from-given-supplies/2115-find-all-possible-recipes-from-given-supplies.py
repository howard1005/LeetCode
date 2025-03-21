class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ansl = []

        rd = set(recipes)

        inds = defaultdict(int)
        ed = defaultdict(set)

        for r,l in zip(recipes,ingredients):
            inds[r] += len(l)
            for ing in l:
                ed[ing].add(r)
            

        dq = deque(supplies)
        while dq:
            i = dq.popleft()
            for ni in ed[i]:
                inds[ni] -= 1
                if inds[ni] == 0:
                    if ni in rd:
                        ansl.append(ni)
                    dq.append(ni)

        return ansl
