class Solution:
    def countOfAtoms(self, formula: str) -> str:
        l = []

        prev = ''
        for c in formula:
            if c.isupper():
                if prev:
                    l.append(prev)
                prev = c
            elif c.isdigit():
                if prev.isdigit():
                    prev += c
                elif prev == '':
                    prev += c
                else:
                    if prev:
                        l.append(prev)
                    prev = c
            elif c in '()':
                if prev:
                    l.append(prev)
                prev = ''
                l.append(c)
            else:
                prev += c
        if prev:
            l.append(prev)
        # print(l)

        def add_update(d1,d2):
            for k,v in d2.items():
                d1[k] += v

        def parse(i):
            d = defaultdict(int)
            prev = {}
            while i<len(l):
                s = l[i]
                if s.isdigit():
                    n = int(s)
                    for k,v in prev.items():
                        prev[k] *= n
                    add_update(d,prev)
                    prev = {}
                elif s == '(':
                    j,dd = parse(i+1)
                    add_update(d,prev)
                    prev = dd
                    i = j
                    continue
                elif s == ')':
                    add_update(d,prev)
                    return i+1,d
                else:
                    add_update(d,prev)
                    prev = {s:1}
                    
                i += 1

            add_update(d,prev)

            return i,d
                

        _,d = parse(0)

        # print(d)

        ld = [(k,v) for k,v in d.items()]
        ld.sort()

        ans = ''
        for k,v in ld:
            ans += k
            if v > 1:
                ans += str(v)


        return ans