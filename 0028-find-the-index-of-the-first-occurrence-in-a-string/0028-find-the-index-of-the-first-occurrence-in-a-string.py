class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a=list(haystack)
        b=list(needle)
        l1=[]
        for i in range(len(a)):
            if i+len(b)>len(a):
                break
            l1=a[i:i+len(b)]
            if l1==b:
                return i
        return -1


        