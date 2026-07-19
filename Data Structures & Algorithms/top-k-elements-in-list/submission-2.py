class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l =[]
        for n in nums: 
            if n in d: 
                d[n]+=1
            else:
                d[n]=1
        l = sorted(d.keys(), key=lambda x: d[x], reverse=True)
        return l[:k]