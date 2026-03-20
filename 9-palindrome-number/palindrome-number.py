class Solution(object):
    def isPalindrome(self, x):
        num=x
        rev=0
        while num>0:
            digit=num%10
            num//=10
            rev=rev*10+digit
        if (x <= 2**31 - 1) or (x>=-2**31 ):
            if(rev==x):
                return True
            else:
                return False
        