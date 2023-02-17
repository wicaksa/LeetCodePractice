class Solution {
    public int firstUniqChar(String s) {
        
        // Used a linked hash map to preserve order
        Map<Character, Integer> hashMap = new LinkedHashMap<>(); 
        
        char c;
        
        for (int i = 0; i < s.length(); i++) {
            
            c = s.charAt(i);
            
            if (!hashMap.containsKey(c)) {
                
                hashMap.put(c, 1);
                
            } else {
                
                hashMap.put(c, hashMap.get(c) + 1);
            }
        }
        
        for (Map.Entry<Character, Integer> e : hashMap.entrySet()) {
            
            if (e.getValue() == 1) {
                
                return s.indexOf(e.getKey());
            }
        }
        return -1;
    }
}