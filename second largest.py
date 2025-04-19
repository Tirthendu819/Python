class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n=len(arr)
        arr.sort()
        x=arr[n-1]
        for i in range(n-1,-1,-1):
            if(arr[i]!=arr[i-1]):
                return arr[i-1]
        return -1;