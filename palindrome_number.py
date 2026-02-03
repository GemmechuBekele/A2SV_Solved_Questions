class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # Negative numbers can't be palindrome
            return False
        elif x % 10 == 0 and x != 0: 
            #number ending with zero is not palindrome except zero itself
            return False 
        reversed_num = 0

        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10
        return x == reversed_num or x == reversed_num // 10
solution = Solution()