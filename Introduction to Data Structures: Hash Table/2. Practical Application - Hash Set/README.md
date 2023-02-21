# Hash Set - Usage

The hash set is one of the implementations of a set which is a data structure to store no repeated values. 

We provide an example of using the hash set in Java, C++ and Python. If you are not familiar with the usage of the hash set, it will be helpful to go through the example.

## Python

```python
# 1. initialize the hash set
hashset = set() 

# 2. add a new key
hashset.add(3)
hashset.add(2)
hashset.add(1)

# 3. remove a key
hashset.remove(2)

# 4. check if the key is in the hash set
if (2 not in hashset):
    print("Key 2 is not in the hash set.")

# 5. get the size of the hash set
print("Size of hashset is:", len(hashset)) 

# 6. iterate the hash set
for x in hashset:
    print(x, end=" ")
print("are in the hash set.")

# 7. clear the hash set
hashset.clear()                         
print("Size of hashset:", len(hashset))
```

```java
// "static void main" must be defined in a public class.
public class Main {
    public static void main(String[] args) {
        // 1. initialize the hash set
        Set<Integer> hashSet = new HashSet<>();     

        // 2. add a new key
        hashSet.add(3);
        hashSet.add(2);
        hashSet.add(1);

        // 3. remove the key
        hashSet.remove(2);        

        // 4. check if the key is in the hash set
        if (!hashSet.contains(2)) {
            System.out.println("Key 2 is not in the hash set.");
        }

        // 5. get the size of the hash set
        System.out.println("The size of has set is: " + hashSet.size());     

        // 6. iterate the hash set
        for (Integer i : hashSet) {
            System.out.print(i + " ");
        }

        System.out.println("are in the hash set.");
        // 7. clear the hash set
        hashSet.clear();

        // 8. check if the hash set is empty
        if (hashSet.isEmpty()) {
            System.out.println("hash set is empty now!");
        }
    }
}
```

#  Find Duplicates By Hash Set

As we know, it is easy and effective to insert a new value and check if a value is in a hash set or not.

Therefore, typically, a hash set is used to check if a value has ever appeared or not.
 
## Example

Let's look at an example:

    Given an array of integers, find if the array contains any duplicates. 

This is a typical problem which can be solved by a hash set.

You can simply iterate each value and insert the value into the set. If a value has already been in the hash set, there is a duplicate.

```java
/*
 * Template for using hash set to find duplicates.
 */
boolean findDuplicates(List<Type> keys) {
    // Replace Type with actual type of your key
    Set<Type> hashset = new HashSet<>();
    for (Type key : keys) {
        if (hashset.contains(key)) {
            return true;
        }
        hashset.add(key);
    }
    return false;
}
```
