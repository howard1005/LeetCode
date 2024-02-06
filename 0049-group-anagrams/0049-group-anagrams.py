from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i,s in enumerate(strs):
            ts = tuple(sorted(list(s)))
            d[ts].append(i)
        ans = []
        for l in d.values():
            ans.append([strs[i] for i in l])
        return ans