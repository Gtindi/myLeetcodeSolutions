class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) != str(x)[::-1]: return False
        if str(x) == str(x)[::-1]: return True   
        return
    
