class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)
        ss.sort()
        tt = list(t)
        tt.sort()
        if len(tt) == len(ss):
            for i in range(len(ss)):
                if ss[i] != tt[i]:
                    return False
            return True
        return False
