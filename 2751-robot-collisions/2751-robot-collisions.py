class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        ansl = []
        
        l = [(p,h,d,i) for i,(p,h,d) in enumerate(zip(positions,healths,directions))]
        l.sort()

        st = []

        for p,h,d,i in l:
            if d == 'R':
                st.append((i,h))
            else:
                while st and h:
                    ti,th = st.pop()
                    if th < h:
                        h -= 1
                    elif th > h:
                        st.append((ti,th-1))
                        h = 0
                    else:
                        h = 0
                if h:
                    ansl.append((i,h))
        
        ansl.extend(st)
        ansl.sort()

        return [h for _,h in ansl]
