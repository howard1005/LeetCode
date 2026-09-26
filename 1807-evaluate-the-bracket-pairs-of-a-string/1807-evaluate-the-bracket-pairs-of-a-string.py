class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = defaultdict(lambda:"?")

        for k,v in knowledge:
            d[k] = v

        s = s.replace('(','{').replace(')','}')

        return s.format_map(d)