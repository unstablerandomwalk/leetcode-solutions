class Solution {
    public int findDuplicate(int[] nums) {
        boolean seen [] = new boolean [nums.length + 1];
        for (int i = 0; i < nums.length; i++){
            if (seen[nums[i]] == true){
                return nums[i];
            } else {
                seen[nums[i]] = true;
            }
        }
        return -1;
    }
}