class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        
        HashMap <String, Integer> hashMap = new HashMap <> (); 
        
        List arr2 = Arrays.asList(list2);
        
        ArrayList<String>res = new ArrayList <> (); 
        
        String [] result; 
        
        String word;
        
        int minVal;
        
        int index = 0;
        
        for (int i = 0; i < list1.length; i++) {
            
            word = list1[i];
            
            if (arr2.contains(word)) {
                
                hashMap.put(word, i + arr2.indexOf(word));
                
            }
        }
        
        minVal = Collections.min(hashMap.values());
        
        for ( Map.Entry<String, Integer> e : hashMap.entrySet() ){
            
            String key = e.getKey();
            Integer val = e.getValue();
            
            if (val == minVal) {
                
                res.add(key);
            }
        }
        
        result = new String [res.size()];
        
        res.toArray(result);
        
        return result;
        
    }
}