##### Not able to solve #############


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def fun(i, j, res, ari, arj):
            # base case
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            
            #recursive
            for k in range(2):
                ni = i + ari[k]
                nj = j + arj[k]
                res += ni + nj
                if ni > 0 and nj < 0 and ni < m and nj < n:
                    fun(ni, nj, res, ari, arj)
            return res
        res = 0
        ari = [0, 1]
        arj = [1, 0]
        return fun(0,0, res, ari,arj)
        