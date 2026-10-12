class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}
        for x,y in zip(s,t):
            d1[x] = d1.get(x, 0) + 1
            d2[y] = d2.get(y, 0) + 1
        return d1 == d2
