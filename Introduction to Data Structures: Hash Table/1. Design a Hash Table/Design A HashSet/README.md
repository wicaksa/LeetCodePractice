# Design HashSet

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

- void add(key) Inserts the value key into the HashSet.
- bool contains(key) Returns whether the value key exists in the HashSet or not.
- void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

## Example

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1); // set = [1]
myHashSet.add(2); // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2); // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2); // set = [1]
myHashSet.contains(2); // return False, (already removed)

## Constraints

- 0 <= key <= 106
- At most 104 calls will be made to add, remove, and contains.

## Approach

1. Program: This is a simple HashSet Implementation. Essentially, we create a list to store the data.
   The list will initially contain False values. When we want to insert a key, we will go into that index
   and change the value of the array to False (Vice versa for removing). To check whether or not the list contains
   a specific value, we just check that index and see what the value stored is.
   There is no implementation of a hashkey since we use the value given as a parameter as the key for the array.

## Complexity For First Approach

1. Time: O(1) - Constant Lookup.
2. Space: O(N) - Not good since it's quite high.
