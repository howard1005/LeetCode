class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0]*26 for _ in range(rows)]

    def _get_idx(self, cell: str):
        c = cell[0]
        n = int(cell[1:])
        return n-1,ord(c)-ord('A')
        

    def setCell(self, cell: str, value: int) -> None:
        i,j = self._get_idx(cell)
        self.grid[i][j] = value
        

    def resetCell(self, cell: str) -> None:
        i,j = self._get_idx(cell)
        self.grid[i][j] = 0

    def getValue(self, formula: str) -> int:
        c1,c2 = formula[1:].split('+')
        ret = 0
        if c1.isdigit():
            ret += int(c1)
        else:
            i,j = self._get_idx(c1)
            ret += self.grid[i][j]
        if c2.isdigit():
            ret += int(c2)
        else:
            i,j = self._get_idx(c2)
            ret += self.grid[i][j]
        return ret
        
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)