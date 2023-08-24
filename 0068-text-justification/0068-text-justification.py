class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def proc(l):
            ret = ''
            if len(l) == 1:
                ret = l[0] + ' '*(maxWidth-len(l[0]))
            elif len(l) > 1:
                remain = maxWidth - len(''.join(l))
                space = remain//(len(l)-1)
                extra = remain%(len(l)-1)
                for word in l[:-1]:
                    ret += word + ' '*space
                    if extra:
                        ret += ' '
                        extra -= 1
                ret += l[-1]
            return ret
        
        ans = []
        l = []
        remain = maxWidth
        i = 0
        while i < len(words):
            word = words[i]
            if len(word) <= remain:
                l.append(word)
                remain -= len(word)+1
                i += 1
            else:
                ans.append(proc(l))
                l = []
                remain = maxWidth
        if l:
            last = ' '.join(l)
            last += ' '*(maxWidth-len(last))
            ans.append(last)
            
        return ans
                