class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs=0
        maxi=float('-inf')
        for num in nums:
            cs+=num
            maxi=max(cs,maxi)
            if(cs<0):
                cs=0
        return maxi        