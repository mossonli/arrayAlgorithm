class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            False
        str_x = str(x)
        y = str_x[::-1]
        y = int(y)
        if x == y:
            return True