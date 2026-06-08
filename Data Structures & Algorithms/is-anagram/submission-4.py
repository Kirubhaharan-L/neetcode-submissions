class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = list(s)
        for char in t:
            if char in res:
                res.remove(char)
            else:
                return False
        if res == []:
            return True
        return False
        