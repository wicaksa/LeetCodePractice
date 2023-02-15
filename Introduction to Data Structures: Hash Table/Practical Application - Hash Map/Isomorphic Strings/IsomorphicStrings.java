class Solution {
    public boolean isIsomorphic(String s, String t) {
        
        HashMap<Character,Character> hashMap = new HashMap<>(); 
        
        for (int i = 0; i < s.length(); i++) {
            if (!hashMap.containsKey(s.charAt(i))) {
                if (!hashMap.containsValue(t.charAt(i))) {
                    hashMap.put(s.charAt(i), t.charAt(i));
                }
                else {
                    return false;
                }
            } else {
                if (hashMap.get(s.charAt(i)) != t.charAt(i)) {
                    return false;
                }
            }
        }
        return true;
    }
}