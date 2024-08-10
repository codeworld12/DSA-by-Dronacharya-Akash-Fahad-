class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)
        f = strs[0]
        l = strs[-1]
        for i in range(len(f)):
            if f[i] != l[i]:
                return ans
            ans += f[i]
        return ans 