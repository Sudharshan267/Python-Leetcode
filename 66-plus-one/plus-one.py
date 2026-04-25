class Solution(object):
    def plusOne(self, digits):
        number = int("".join(map(str, digits)))
        number+=1
        plus_num=str(number)
        plus_digits=[]
        for i in plus_num:
            plus_digits.append(int(i))
        return plus_digits



        