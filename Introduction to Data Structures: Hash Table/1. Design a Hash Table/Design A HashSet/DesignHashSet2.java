// create a fixed set of buckets
// map the range of inputs to these buckets
// handle collisions by using a list for each bucket

class MyHashSet {
    
    // initialize constant for the max value for key
    private final int MAX_VALUE = 1000000;
    
    // initialize an array size for your bucket (can be any number)
    private final int ARRAY_SIZE = 100;
    
    // initialize a list for each bucket
    private List<List<Integer>> parentList;

    public MyHashSet() {
        
        // initialize parentList with ARRAY_SIZE
        parentList = new ArrayList<>(ARRAY_SIZE);
        
        // initialize null values to parentList
        for (int i = 0; i < ARRAY_SIZE; i++) {
            parentList.add(null);
        }
    }
    
    public void add(int key) {
        
        // find an index value using a simple hashing algorithm
        int index = key % ARRAY_SIZE; 
        
        // use the index from the previous calculation to see if the parentList has 
        // a childList at that particular index
        List<Integer> childList = parentList.get(index);
        
        // if there is no childList yet
        if (childList == null) {
            
            // initialize a new linked list
            List<Integer> list = new LinkedList<>();
            
            // add the key to the linked list 
            list.add(key);
            
            // add the linked list to the parent list at the current index
            parentList.set(index, list);
        }
        else {
            
            // if the childList is not null
            if (!childList.contains(key)) {
                
                // simply add the key to the childList
                childList.add(key);
            }
        }
    }
    
    public void remove(int key) {
        
        // get an index using a simple hashing algorithm
        int index = key % ARRAY_SIZE;
        
        // use the index to see if there is a list at the index of paretList
        List<Integer> childList = parentList.get(index);
        
        // if there is a childList 
        if (childList != null) {
            
            // simply remove the instance of the key value from the linked list
            // remember box key to an integer to remove the correct object and not the 
            // element at the index
            childList.remove(Integer.valueOf(key));
        }
    }
    
    public boolean contains(int key) {
        
        // get an index using a simple hashing algorithm
        int index = key % ARRAY_SIZE; 
        
        // use the index to see if there is a list at the index of paretList
        List<Integer> childList = parentList.get(index);
        
        // if the childList is not null AND the childList contains the key value
        if (childList != null && childList.contains(key)) {
            
            // return true
            return true;
        }
        else {
            
            // return false otherwise
            return false;
        }
    }
}

// Time complexity depends on load factor (how big the bucket size is) and the rehashing algorithm
