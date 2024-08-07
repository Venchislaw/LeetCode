class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""

        for char in s:
            if char.isalnum():
                string += char.lower()

        l = 0
        r = len(string) - 1

        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1

        return True
