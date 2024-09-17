class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1=s1.split(" ")
        l2=s2.split(" ")
        
        d=defaultdict(int)
        
        for w in l1+l2:
            d[w]+=1
            
        ansl=[]
        
        for k,v in d.items():
            if v == 1:
                ansl.append(k)
                
        return ansl
            