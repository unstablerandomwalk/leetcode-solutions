class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount
        for coin in coins:
            for n in range(coin, amount + 1):
                if dp[n - coin] + 1 < dp[n]:
                    dp[n] = dp[n - coin] + 1
        return dp[amount] if dp[amount] <= amount else -1