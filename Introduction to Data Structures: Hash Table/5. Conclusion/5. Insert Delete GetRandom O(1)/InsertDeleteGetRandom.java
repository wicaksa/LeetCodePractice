
class RandomizedSet {
    
    private Map<Integer, Integer> hashMap;
    private List<Integer> arrayList;
    
    public RandomizedSet() {
        hashMap = new HashMap<Integer, Integer>();
        arrayList = new ArrayList<>();
    }
    
    public boolean insert(int val) {
        
        if (hashMap.containsKey(val)) {
            return false;
        } else {
            arrayList.add(val);
            hashMap.put(val, arrayList.indexOf(val));
            return true;
        }
    }
    
    public boolean remove(int val) {
        if (hashMap.containsKey(val)) {
            
            // get the index of val in arraylist
            int currIndex = hashMap.get(Integer.valueOf(val));
            
            // get the element at the end of array list
            int lastElement = arrayList.get(arrayList.size() - 1);
            
            // replace the removed element with last element
            arrayList.set(currIndex, lastElement);
            
            // remove element at the end of arrayList
            arrayList.remove(arrayList.size() - 1);
            
            // replace mapping for last element
            hashMap.put(lastElement, currIndex);
            
            // remove value from hashMap
            hashMap.remove(Integer.valueOf(val));
                
            return true;
            
        } else {
            
            return false;
        }
    }
    
    public int getRandom() {
        // generate a random number from 0 - max size of arraylist
        int randomIndex = (int) (Math.random() * (arrayList.size()));
        
        // return the element at that index
        return arrayList.get(randomIndex);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */