class Solution:
    def reverseWords(self, s: str) -> str:
        return ''.join(map(lambda x:x.replace(' ','') if x == '' else x+' ',s.split(' ')[::-1])).strip()