class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_S = {}
        hashmap_T = {}
        if len(s) != len(t):
            return False
        for char in s:
            hashmap_S[char] = 1 + hashmap_S.get(char, 0)
        for char in t:
            hashmap_T[char] = 1 + hashmap_T.get(char, 0)
        return hashmap_S == hashmap_T