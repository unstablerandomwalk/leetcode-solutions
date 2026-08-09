class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        i,j=0,0
        total = 0
        while i < len(prices) and j < len(discounts):
            total += prices[i] * (100-discounts[j])/100
            i+=1
            j+=1
        while i < len(prices):
            total += prices[i]
            i+=1
        return total