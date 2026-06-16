class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i , j = 0 , n -1
        if n == 1:
            return True
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i , j = i+1, j-1
        return True
