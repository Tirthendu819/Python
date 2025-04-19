class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ans=1
        for i in range(len(nums)):
            if(nums[i]==ans):
                ans=ans+1
            elif(nums[i]>ans):
                return ans    
        return ans