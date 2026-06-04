from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t) # Using Counter
        
        # Without Using Counter
            # if len(s) != len(t):
            #     return False
            # count = {}

            # for i in range(len(s)):
            #     count[s[i]] = 1 + count.get(s[i], 0)
            #     count[t[i]] = count.get(t[i],0) - 1
            
            # for val in count.values():
            #     if val != 0:
            #         return False
            # return True
