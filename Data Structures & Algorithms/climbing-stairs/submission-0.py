class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        prev = 1
        current = 2
        for i in range(2, n):
            next_value = prev + current
            prev = current
            current = next_value
        
        return current


        