class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=height
        left=0
        right=len(a)-1
        max=0
        while left<right:
            height=min(a[left],a[right])
            w=right-left
            res=height*w
            if res>max:
                max=res
            if a[left]<a[right]:
                left+=1
            else:
                right-=1
        return max
        