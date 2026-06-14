class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_formatted = ''
        for i in s[::-1]:
            if i.isalnum():
                s_formatted += i.lower()
        return s_formatted == s_formatted[::-1]