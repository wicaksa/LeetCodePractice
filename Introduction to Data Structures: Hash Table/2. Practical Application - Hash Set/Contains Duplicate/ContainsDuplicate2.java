class Solution {
    public boolean containsDuplicate(int[] nums) {
        // create a HashSet
        HashSet<Integer> set = new HashSet<>();
        
        // loop through nums
        for (int num : nums) {
            
            if (set.contains(num)) {
                
                return true;
            } 
            
            else {
                set.add(num);
            }
        }
        return false;
    }
}