class Solution(object):
    def lengthOfLastWord(self, s):
        subs=s.split()
        length=len(subs)
        last_word=subs[length-1]
        letter=len(last_word)
        return letter