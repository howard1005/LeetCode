class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A,B = 0,0
        a,b = 0,0
        for c in colors:
            if c == 'A':
                B += max(0,b-2)
                b = 0
                a += 1
            else:
                A += max(0,a-2)
                a = 0
                b += 1
        if a:
            A += max(0,a-2)
        if b:
            B += max(0,b-2)

        return A>B