class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        while True:
            new_dominoes = dominoes.replace('R.L', '|').replace('.L', 'LL').replace('R.', 'RR').replace('|', 'R.L')
            if new_dominoes == dominoes:
                break
            else:
                dominoes = new_dominoes
            
        return dominoes
