class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            number = str(x)
            ran = len(number)
            pal = ""
            for i in range(1, ran + 1):
                pal += number[-i]

            x2 = int(pal)
            return x == x2

