class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        
        // counter 
        int output = 0;
        
        int sum;
        int key;
        
        // create hash map for sums of nums1 and nums2
        Map<Integer, Integer> hashMap = new HashMap<>();
        
        for (int num1 : nums1) {
            
            for (int num2 : nums2) {
                
                sum = num1 + num2;
                
                hashMap.put(sum, hashMap.getOrDefault(sum, 0) + 1);
            }
        }
        
        // for loop through nums3
        for (int num3 : nums3) {
            
            // for loop through nums 4
            for (int num4 : nums4) {
                
                key = (num3 + num4) * (-1);
                
                output = output + hashMap.getOrDefault(key, 0);
            }
        }
        
        // return counter
        return output;
    }
}