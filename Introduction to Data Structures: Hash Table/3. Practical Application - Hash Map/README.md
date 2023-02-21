# Hash Map - Usage

The hash map is one of the implementations of a map which is used to store (key, value) pairs.

We provide an example of using the hash map in Java, C++ and Python. If you are not familiar with the usage of the hash map, it will be helpful to go through the example.

```java
// "static void main" must be defined in a public class.
public class Main {
    public static void main(String[] args) {
        // 1. initialize a hash map
        Map<Integer, Integer> hashmap = new HashMap<>();

        // 2. insert a new (key, value) pair
        hashmap.putIfAbsent(0, 0);
        hashmap.putIfAbsent(2, 3);

        // 3. insert a new (key, value) pair or update the value of existed key
        hashmap.put(1, 1);
        hashmap.put(1, 2);

        // 4. get the value of specific key
        System.out.println("The value of key 1 is: " + hashmap.get(1));

        // 5. delete a key
        hashmap.remove(2);

        // 6. check if a key is in the hash map
        if (!hashmap.containsKey(2)) {
            System.out.println("Key 2 is not in the hash map.");
        }

        // 7. get the size of the hash map
        System.out.println("The size of hash map is: " + hashmap.size());

        // 8. iterate the hash map
        for (Map.Entry<Integer, Integer> entry : hashmap.entrySet()) {
            System.out.print("(" + entry.getKey() + "," + entry.getValue() + ") ");
        }
        System.out.println("are in the hash map.");

        // 9. clear the hash map
        hashmap.clear();

        // 10. check if the hash map is empty
        if (hashmap.isEmpty()) {
            System.out.println("hash map is empty now!");
        }
    }
}
```

```python
# 1. initialize a hash map
hashmap = {0 : 0, 2 : 3}

# 2. insert a new (key, value) pair or update the value of existed key
hashmap[1] = 1
hashmap[1] = 2

# 3. get the value of a key
print("The value of key 1 is: " + str(hashmap[1]))

# 4. delete a key
del hashmap[2]

# 5. check if a key is in the hash map
if 2 not in hashmap:
    print("Key 2 is not in the hash map.")

# 6. both key and value can have different type in a hash map
hashmap["pi"] = 3.1415

# 7. get the size of the hash map
print("The size of hash map is: " + str(len(hashmap)))

# 8. iterate the hash map
for key in hashmap:
    print("(" + str(key) + "," + str(hashmap[key]) + ")", end=" ")
print("are in the hash map.")

# 9. get all keys in hash map
print(hashmap.keys())

# 10. clear the hash map
hashmap.clear();
print("The size of hash map is: " + str(len(hashmap)))
```

# Scenario I - Provide More Information

The first scenario to use a hash map is that we need more information rather than only the key. Then we can build a mapping relationship between key and information by hash map.
 
## An Example

Let's look at an example:

    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

In this example, if we only want to return true if there is a solution, we can use a hash set to store all the values when we iterate the array and check if target - current_value is in the hash set or not.

However, we are asked to return more information which means we not only care about the value but also care about the index. We need to store not only the number as the key but also the index as the value. Therefore, we should use a hash map rather than a hash set.
 
## What's More

In some cases, we need more information not just to return more information but also to help us with our decisions.

In the previous examples, when we meet a duplicated key, we will return the corresponding information immediately. But sometimes, we might want to check if the value of the key is acceptable first.
 
## Template

Here we provide a template for you to solve this kind of problems:

```java
/*
 * Template for using hash map to find duplicates.
 * Replace ReturnType with the actual type of your return value.
 */
ReturnType aggregateByKey_hashmap(List<Type>& keys) {
    // Replace Type and InfoType with actual type of your key and value
    Map<Type, InfoType> hashmap = new HashMap<>();
    
    for (Type key : keys) {
        if (hashmap.containsKey(key)) {
            if (hashmap.get(key) satisfies the requirement) {
                return needed_information;
            }
        }
        // Value can be any information you needed (e.g. index)
        hashmap.put(key, value);    
    }
    return needed_information;
}
```