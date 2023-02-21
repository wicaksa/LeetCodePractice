class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        int p1 = 0;
        int p2 = 0;
        int i = 0;
        
        List<Integer> temp = new ArrayList<>(); 
        
        int [] res;
        
        while (p1 < nums1.length && p2 < nums2.length) {
            
            if (nums1[p1] == nums2[p2]) {
                
                temp.add(nums1[p1]);
                
                p1++;
                p2++;
                
            } else if (nums1[p1] < nums2[p2]) {
                
                p1++;
                
            } else {
                
                p2++;
                
            }
        }
        
        res = new int [temp.size()];
        
        for (Integer value : temp) {
            
            res[i++] = value;
            
        }
        
        return res;
        
    }
}