# the s and t are two diff word and s should be rplaceable with t but unique characters can replace in unique s.




class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sett = set()
        for i in s:
            sett.add(i)
        bett = set()
        for i in t:
            bett.add(i)
        if len(sett) == len(bett):
            return True
        return False