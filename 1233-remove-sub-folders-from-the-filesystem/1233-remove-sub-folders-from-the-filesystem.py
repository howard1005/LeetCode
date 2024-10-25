class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        
        folder.sort(key=lambda x: len(x))

        sd = set()
        
        def valid(f):
            s = ''
            for c in f:
                if c == '/' and s in sd:
                    return False
                s += c

            return True


        for f in folder:
            if valid(f):
                ans.append(f)
            sd.add(f)

        return ans 