class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        
        Map<Character, Integer> hashMap = new HashMap<>();
        
        int total = 0;
        
        for (int i = 0; i < jewels.length(); i++) {
            hashMap.put(jewels.charAt(i), 0);
        }
        
        for (int i = 0; i < stones.length(); i++) {
            if (hashMap.containsKey(stones.charAt(i))) {
                total += 1;
            }
        }
        
        return total;
    }
}