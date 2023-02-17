class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        
        Map<Integer, Integer> hashMap = new HashMap<Integer, Integer>(); 
        
        ArrayList<Integer> tempResult = new ArrayList<Integer>();
        
        int [] result;
        
        for (int i : nums1) {
            
            if (!hashMap.containsKey(i)) {
                
                hashMap.put(i, 1);
            } else {
                
                hashMap.put(i, hashMap.get(i) + 1);
            }
        }
        
        for (int i : nums2) {
            
            if (hashMap.containsKey(i)) {
                
                if (hashMap.get(i) != 0) {
                    
                    tempResult.add(i);
                    
                    hashMap.put(i, hashMap.get(i) - 1);
                }
            }
        }
        
        result = new int [tempResult.size()];
        int index = 0;
        
        for (Integer val : tempResult) {
            result[index++] = val;
        }
        
        return result;
    }
}