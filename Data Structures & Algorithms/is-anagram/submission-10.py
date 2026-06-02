class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrange_s = sorted(s)
        arrange_t = sorted(t)
        if len(arrange_s) != len(arrange_t):
            return False
        return arrange_s == arrange_t
        