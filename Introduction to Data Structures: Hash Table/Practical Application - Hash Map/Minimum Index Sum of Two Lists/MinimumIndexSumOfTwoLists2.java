class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        
        // create a hashmap to store key, value from list 1
        HashMap<String, Integer> hashMap = new HashMap<>();
        
        // create an arraylist to store the result
        ArrayList<String> result = new ArrayList<>(); 
        
        
        // keep track of min value
        int min = Integer.MAX_VALUE;
        
        // keep track of total sum of indices
        int total;
        
        // iterate through list 1 and store key value pairs ->  (word, index)
        for (int i = 0; i < list1.length; i++) {
            
            hashMap.put(list1[i], i);
            
        }
        
        // iterate through list2 
        for (int i = 0; i < list2.length; i++) {
            
            // reset the total
            total = 0;
            
            // if the hash map has the current word in list2 as a key
            if (hashMap.containsKey(list2[i])) {
                
                // get the total sum of indices by getting current index + value of the hash map at the current key
                total = i + hashMap.get(list2[i]);
                
                // if the total sum of indices is less than the current min value
                if (total < min) {
                    
                    // set the min value to the total
                    min = total;
                    
                    // clear the current result
                    result.clear();
                    
                    // add the word to the result list
                    result.add(list2[i]);
                    
                // if the total == min
                } else if (total == min) {
                    
                    // just add the word to the result
                    result.add(list2[i]);
                }
            }
        }
        
        // convert the arraylist to an array and return 
        
        // create a new array of size result
        String [] output = new String [result.size()];
        
        // use the toArray() method to return the arraylist as an array
        return result.toArray(output);
        
    }
}