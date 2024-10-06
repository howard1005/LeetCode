class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        l1,l2 = sentence1.split(" "),sentence2.split(" ")

        def proc(l1,l2):
            for i in range(len(l1)+1):
                al = l1[:i]
                bl = l1[i:]
                tal = l2[:len(al)]
                tbl = l2[-len(bl):] if bl else []
                # print(i,al,bl,tal,tbl)
                if al == tal and bl == tbl:
                    return True
            return False

        return proc(l1,l2) or proc(l2,l1)