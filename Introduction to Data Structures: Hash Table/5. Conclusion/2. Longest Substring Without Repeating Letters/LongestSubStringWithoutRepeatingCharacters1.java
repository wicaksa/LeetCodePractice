class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        Set<Character> hashSet = new HashSet<>(); 
        
        int l = 0;
        
        int r = 0;
        
        int max = 0;
        
        while (r < s.length()) {
            
            if (!hashSet.contains(s.charAt(r))) {
                
                hashSet.add(s.charAt(r));
                
                max = Math.max(max, hashSet.size());
                
                r++; 
                
            } else {
                
                hashSet.remove(s.charAt(l));
                
                l++;
            }
        }
        
        return max;
    
    }
}