class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = list(map(lambda x : int(x), version1.split('.')))
        l2 = list(map(lambda x : int(x), version2.split('.')))
        length1,length2 = len(l1),len(l2)
        if length1 < length2:
            for _ in range(length2-length1):
                l1.append(0)
        if length1 > length2:
            for _ in range(length1-length2):
                l2.append(0)
        for i in range(max(length1,length2)):
            n1,n2 = l1[i],l2[i]
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
        return 0