class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_a=set(nums1)
        result=set()

        for i in nums1:
            if i in nums2:
                result.add(i)

        return list(result)  