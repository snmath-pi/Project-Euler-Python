class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s,cur=0,-inf
        for n in nums:
            s+=n
            cur=max(cur,s)
            if s<0:
                s=0
        return cur