class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        ans = []

        le = len(nums)

        exp = 1
        while (1<<exp) < le:
            exp += 1
        size = 1<<exp
        tree_size = size*2
        # print('size',size)

        tree = [[0 for _ in range(k+1)] for _ in range(tree_size)]

        def merge(r1, r2):
            if not r1:
                return r2
            if not r2:
                return r1

            r = [0] * (k + 1)

            for j in range(k):
                r[j] += r1[j]
                r[r1[k] * j % k] += r2[j]

            r[k] = r1[k] * r2[k] % k
            return r

        def query(us,ue,i=1,s=0,e=size-1):
            if e < us or ue < s:
                return None
            if us <= s and e <= ue:
                return tree[i]
 
            r = [0]*(k+1)
 
            m = (s+e)//2
        
            r1 = query(us,ue,i*2,s,m)
            r2 = query(us,ue,i*2+1,m+1,e)

            return merge(r1,r2)

        
        def update(us,ue,uv,i=1,s=0,e=size-1):
            # print(i,s,e)
            if e < us or ue < s:
                return tree[i]
            if us <= s and e <= ue:
                if uv == None:
                    tree[i] = None
                    return tree[i]
                r = [0]*(k+1)
                r[uv] = 1
                r[k] = uv
                # print(i)
                tree[i] = r
                return tree[i]
 
            r = [0]*(k+1)
 
            m = (s+e)//2
        
            r1 = update(us,ue,uv,i*2,s,m)
            r2 = update(us,ue,uv,i*2+1,m+1,e)

            tree[i] = merge(r1, r2)
            return tree[i]


        for idx in range(size):
            if idx < le:
                uv = nums[idx] % k
                r = [0] * (k+1)
                r[uv] = 1
                r[k] = uv
                tree[size+idx] = r
            else:
                tree[size+idx] = None

        for i in range(size-1, 0, -1):
            tree[i] = merge(tree[i*2], tree[i*2+1])

        # level = 0
        # while 2**level < tree_size:
        #     a, b = 2**level, min(2**(level+1), tree_size)
        #     print("   ".join(map(str, tree[a:b])))
        #     level += 1
        # print()

        for idx,v,s,x in queries:
            update(idx,idx,v%k)
            r = query(s,size-1)
            # print(r)
            ans.append(r[x])

        return ans