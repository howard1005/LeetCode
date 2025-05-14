class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 1_000_000_007

        MAXB = 1
        while t >= (1<<MAXB):
            MAXB += 1

        ans = 0

        l = [[[0 for _ in range(26)] for _ in range(26)] for _ in range(MAXB+1)] # List[List[List[tuple]]]

        def get_exp_trees(exp):
            return l[exp]

        def get_chr_leaf_nodes(exp,c):
            i = c
            if isinstance(c, str):
                i = ord(c)-ord('a')
            return l[exp][i]

        def extensed_chr_tree_by_exp(chr_leaf_nodes: List[int], exp):
            l = [0 for _ in range(26)]
            for i in range(len(chr_leaf_nodes)):
                cnt = chr_leaf_nodes[i]
                nodes = get_chr_leaf_nodes(exp,i)
                for j,ncnt in enumerate(nodes):
                    l[j] += cnt*ncnt
                    l[j] %= MOD
            return l
                    
        for i,n in enumerate(nums):
            nodes = get_chr_leaf_nodes(0,i)
            for j in range(i+1,i+n+1):
                m = j%26
                nodes[m] += 1
            
        for exp in range(1,MAXB):
            trees = get_exp_trees(exp)
            for i in range(26):
                nodes = get_chr_leaf_nodes(exp-1,i)
                new_nodes = extensed_chr_tree_by_exp(nodes, exp-1)
                trees[i] = new_nodes

        # for i in range(31):
        #     trees = l[i]
        #     print(i,trees)
        #     print()

        nodes = [0 for _ in range(26)]
        for c in s:
            nodes[ord(c)-ord('a')] += 1
        
        tt = t
        exp = 0
        while tt:
            if tt&1:
                nodes = extensed_chr_tree_by_exp(nodes,exp)
            tt >>= 1
            exp += 1
        ans = sum(nodes)%MOD

        return ans
            