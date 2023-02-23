# Insert Delete GetRandom O(1)

## Implement the RandomizedSet class:

    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

## Examples 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

## Constraints

    -231 <= val <= 231 - 1
    At most 2 * 105 calls will be made to insert, remove, and getRandom.
    There will be at least one element in the data structure when getRandom is called.

## Approach
- Selecting data structures for object: For this problem, I ended up using a hash map and an arraylist/list. The hashmap is good for storing the value that is going to be inserted along with the index that it is stored at in the arraylist/list. This makes it possible to remove an item at constant time since accessing the index of a particular value equates the time to look up that index by accessing the hash map. The array list is neccessary since we need to be able to randomly choose an element to remove. We need a data structure that has continuous indexing. 
- Insert method: This method is simple to implement. We just need to check if the hash map contains the particular key. If it does not, we simply add that key to the hash map with the corresponding value of the length of the arraylist/list. Then, we append that value onto our arraylist/list. 
- Remove method: To do this method in constant time for elements that are in the middle of the array/arraylist, we cannot simply remove it using a built in function. This operation takes linear time since we will have to slide each element after the remove element one space to the left. So to avoid this, we simply get the last element of the array then place it in the index of the element being removed before removing the last element in the array. After, we just need to update the mapping to change the value of the last element to the index of the element being removed. 
- Get random method: In Java, you can use Math.random() * length of the array in order to get a random index from the array before returning that element at that index. In Python, you can simply use random.choice(array) which will choose a random element in the array.

## Review & Evaluate
- Time: O(N) Space: O(M * N)