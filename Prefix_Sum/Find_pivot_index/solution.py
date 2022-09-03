class Solution:
    def pivotIndex(self,nums:List[int])->int:
        leftSide = 0
        total = sum(nums)

        for i in range(len(nums)):
            if (leftSide == total - nums[i] - leftSide):
                return i
            leftSide += nums[i]
        return -1
