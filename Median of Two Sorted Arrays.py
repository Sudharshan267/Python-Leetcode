class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums=sorted(nums1+nums2)
        if (len(nums)%2==0):
            median=(nums[len(nums)//2]+nums[(len(nums)//2)-1]) /2.0
        else:
            median=nums[len(nums)//2]
        return median
