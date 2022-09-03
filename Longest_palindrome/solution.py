class Solution:
    def longestPalindrome(self, s:str)->int:
        c = counter(s)
        output = 0
        odd_found = False

        for count in c.values():
            if odd_found:
                if count > 1:
                    if count % 2 == 0:
                        output += count
                    else:
                        output += count - 1
            else:
                if count % 2 == 0:
                    output += count
                else:
                    output += count
                    odd_found = True
        return output
