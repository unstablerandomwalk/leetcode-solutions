class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int minLength = Integer.MAX_VALUE;
        int start = 0;
        int currSum = 0;
        for (int end = 0; end < nums.length; end++) {
            currSum += nums[end];
            while (currSum >= target) {
                minLength = Math.min(minLength, end - start + 1);
                currSum -= nums[start];
                start++;
            }
        }
        return minLength == Integer.MAX_VALUE ? 0 : minLength;
    }
}