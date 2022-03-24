class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [None] * (N+1)
        dp[N] = 0
        dp[N-1] = nums[N-1]
        for i in range(N-2, -1, -1):
            dp[i] = max(dp[i+1], dp[i+2] + nums[i])
        return dp[0]
