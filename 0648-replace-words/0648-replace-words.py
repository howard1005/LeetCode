class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = set()
        for w in dictionary:
            d.add(w)

        l = []
        for w in sentence.split():
            ww = ''
            for c in w:
                ww += c
                if ww in d:
                    break
            l.append(ww)
            

        return ' '.join(l)
            