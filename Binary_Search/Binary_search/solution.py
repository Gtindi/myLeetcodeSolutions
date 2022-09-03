class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            pivot = (l + r) // 2
            if nums[pivot] > target:
                r = pivot - 1
            elif nums[pivot] < target:
                l = pivot + 1
            else:
                return pivot
        return -1        
