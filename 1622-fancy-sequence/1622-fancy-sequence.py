MOD = 1000000007

x = 1
while (1<<x)<100000:
    x+=1

class Fancy:

    def __init__(self):
        self.idx = 0
        self.tree = [0 for _ in range(1<<(x+1))]
        self.add_lazy = defaultdict(int)
        self.mul_lazy = defaultdict(lambda:1)

    def lazy_apply(self,i,s,e):
        self.tree[i] *= self.mul_lazy[i]
        self.tree[i] += self.add_lazy[i]*(e-s+1)
        self.tree[i] %= MOD
        if s < e:
            self.mul_lazy[2*i] *= self.mul_lazy[i]
            self.mul_lazy[2*i] %= MOD
            self.add_lazy[2*i] *= self.mul_lazy[i]
            self.add_lazy[2*i] += self.add_lazy[i]
            self.add_lazy[2*i] %= MOD

            self.mul_lazy[2*i+1] *= self.mul_lazy[i]
            self.mul_lazy[2*i+1] %= MOD
            self.add_lazy[2*i+1] *= self.mul_lazy[i]
            self.add_lazy[2*i+1] += self.add_lazy[i]
            self.add_lazy[2*i+1] %= MOD

        self.mul_lazy[i] = 1
        self.add_lazy[i] = 0

    def query(self,us,ue,i=1,s=0,e=(1<<x)-1):
        if ue < s or e < us:
            return 0
        self.lazy_apply(i,s,e)
        if us <= s and e <= ue:
            return self.tree[i]

        m = (s+e)//2
        lv = self.query(us,ue,2*i,s,m)
        rv = self.query(us,ue,2*i+1,m+1,e)
        
        self.tree[i] = (lv + rv)%MOD

        return self.tree[i]
        

    def update(self,us,ue,op,uv,i=1,s=0,e=(1<<x)-1):
        if ue < s or e < us:
            return
        if us <= s and e <= ue:
            if op == '+':
                self.add_lazy[i] += uv
                
            if op == '*':
                self.add_lazy[i] *= uv
                self.add_lazy[i] %= MOD
                self.mul_lazy[i] *= uv
                self.mul_lazy[i] %= MOD
            return
        
        m = (s+e)//2
        self.update(us,ue,op,uv,2*i,s,m)
        self.update(us,ue,op,uv,2*i+1,m+1,e)

        
    def append(self, val: int) -> None:
        self.update(self.idx,self.idx,'+',val)
        self.idx += 1
        
    def addAll(self, inc: int) -> None:
        self.update(0,self.idx-1,'+',inc)
        # print('add',self.add_lazy,self.mul_lazy)

    def multAll(self, m: int) -> None:
        self.update(0,self.idx-1,'*',m)
        # print('mul',self.add_lazy,self.mul_lazy)

    def getIndex(self, idx: int) -> int:
        if idx>=self.idx:
            return -1
        ret = self.query(idx,idx)
        # print('getidx',self.add_lazy,self.mul_lazy)
        return ret
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)