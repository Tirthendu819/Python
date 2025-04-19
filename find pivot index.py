class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        ts=0
        ls=0
        for i in range(n):
            ts+=nums[i]
        for i in range(n):
            ts-=nums[i]
            
            if(ls==ts):
                return i
            else:
                ls+=nums[i]    

        return -1