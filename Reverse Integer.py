class Solution(object):
    def reverse(self, x):
        sign=-1 if x<=0 else 1
        num=abs(x)
        rev_num=0
        while num>0:
            digit=num%10
            rev_num=rev_num*10+digit
            num//=10
        if (rev_num>=-2**31) and (rev_num<2**31-1):
            return rev_num*sign
        else:
            return 0
