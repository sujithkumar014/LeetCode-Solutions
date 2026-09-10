class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        a = groupSizes
        s = set(a)
        l=[]
        for i in s:
            
            l1=[]
            for j in range(len(a)):
                if i!=len(l1) and i==a[j]:
                    l1.append(j)
                elif i==a[j]:
                    l.append(l1)
                    l1=[]
                    l1.append(j)
            l.append(l1)
        return l
            



        