class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        // Create two HashSets
        // set: One to store the set of elements in nums1
        // intersection: One to store the intersection of nums1 and nums2
        HashSet<Integer> set = new HashSet<Integer>();
        HashSet<Integer> intersection = new HashSet<Integer>();
        
        // Loop through nums1 and add elements to the set
        for (int num1 : nums1) {
            set.add(num1);
        }
        
        // Loop through num2 and add element to intersection iff it is present in set of nums1
        for (int num2 : nums2) {
            if (set.contains(num2)) {
                intersection.add(num2);
            }
        }
        
        // Create an output int array of size intersection HashMap 
        // Convert Integer to int  and store it in the output int array
        int size = intersection.size(); 
        int [] res = new int [size];
        int index = 0;
        
        for (Integer i : intersection) {
            res[index] = i;
            index++;
        }

        // Return result
        return res;
    }
}