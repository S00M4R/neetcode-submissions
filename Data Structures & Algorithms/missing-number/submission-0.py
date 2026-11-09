class Solution:
    def missingNumber(self, nums: List[int]) -> int:
     
        n = len(nums)
        total = 0
        expected_total = 0

        for i in range(n):
            total += nums[i]
            expected_total += i
        
        expected_total += n

        return expected_total - total