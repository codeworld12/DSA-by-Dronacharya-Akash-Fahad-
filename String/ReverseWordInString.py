class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.split()
        ans = ""
        for i in range(len(st)-1, -1, -1):
            ans += st[i]+" "
        return ans[:-1]