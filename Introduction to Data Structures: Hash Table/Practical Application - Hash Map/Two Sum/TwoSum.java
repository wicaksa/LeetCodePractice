class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        Map <Integer, Integer> hashMap = new HashMap<>(); 
        int [] result = new int [2];
        int diff;
        
        for (int i = 0; i < nums.length; i++) {
            
            diff = target - nums[i];
            
            if (hashMap.containsKey(diff)) {
                result[0] = i;
                result[1] = hashMap.get(diff);
                return result;
            }
            else {
                hashMap.put(nums[i], i);
            }
        }
        return result;
    }
}