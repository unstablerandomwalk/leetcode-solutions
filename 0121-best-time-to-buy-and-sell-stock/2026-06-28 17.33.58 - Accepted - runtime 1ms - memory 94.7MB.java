class Solution {
    public int maxProfit(int[] prices) {
        int cost = prices[0];
        int profit = 0;
        for (int i=0;i<prices.length;i++){
            if (cost > prices[i])
                cost = prices[i];
            if (prices[i] - cost > profit)
                profit = prices[i] - cost;
        }
        return profit;
    }
}