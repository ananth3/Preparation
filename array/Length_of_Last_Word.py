class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        if n==0:
            return 0
        if n==1 and s[0]==" ":
            return 0
        new_s = s.strip(" ").split(" ")
        return len(new_s[-1])
