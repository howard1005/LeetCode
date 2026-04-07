class Robot:

    def __init__(self, width: int, height: int):
        self.di = 1
        self.w = width
        self.h = height
        self.r = 2*(width+height)-4
        self.x = 0
        self.y = 0
        self.i = 0
        self.l = self._initl()
        # print(self.l)
        

    def _initl(self):
        dy,dx = [1,0,-1,0],[0,1,0,-1]
        di = 1
        x,y = 0,0
        l = [(x,y,2)]
        r = self.r
        while len(l) <r:
            nx,ny = x+dx[di],y+dy[di]
            if nx<0 or ny<0 or nx>=self.w or ny>=self.h:
                di = (di-1+4)%4
                continue
            x,y = nx,ny
            l.append((x,y,di))
        return l
                

    def step(self, num: int) -> None:
        self.i = (num+self.i)%self.r
        self.x,self.y,self.di = self.l[self.i]
        

    def getPos(self) -> List[int]:
        return (self.x,self.y)
        
        
    def getDir(self) -> str:
        return ("North", "East", "South", "West")[self.di]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()