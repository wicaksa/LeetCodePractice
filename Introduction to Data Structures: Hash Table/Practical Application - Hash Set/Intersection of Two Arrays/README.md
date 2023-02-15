# Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

## Examples

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

## Constraints

    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000

## Approach

### Approach 1
For this problem, my approach was to use a set. I iterate through one of the lists then check if that element is in the second list. If it is, then I add it to the set. The set will not add duplicate values. This can also be done with a regular list but needs an if statement to check if the element is already in the output list. At the end, I just return the set.

### Approach 2
For this problem, I used a two pointer approach and sorted the inputs. Once the inputs are sorted, I iterate through both lists at the same time. At each iteration, I check whether or not the elements are the same. If they are, I add it to a set that holds the result. Then, I increment both pointers. If they are not the same, we check which element is smaller. Once this is determined, I move the pointer that has the smaller element to the right. 
I do this until one of the pointers goes out of range. 

### Approach 3
In this Java approach, I used HashMaps to solve the problem. I created one HashMap to store the set of elements in the first array. I created another HashMap to store values from nums2 that are present in the set. This will be the intersection of nums1 and nums2. After that, I created an int array with a size of the intersection HashMap. To get the final result array, I just iterate through the intersection HashMap and add each value to the output array.

## Review & Evaluate

### Approach 1 Time and Space Complexity
- Time Complexity: O(N^2) since I iterated through a list and with each iteration, checking the other list to see if the value is present. (Not Efficient).
- Space Complexity: O(N+M) since we created a set to hold the output values. 

### Approach 2 Time and Space Complexity
- Time Complexity: 2 * (nlogn) + O(N + M) sice we sorted two arrays and iterating through both arrays with a pointer.
- Space Complexity: O(N+M) since we created a set to hold the output values. 

### Approach 3 Time and Space Complexity
- Time Complexity: O(N+M) since we iterate through nums1 and nums2 that may have different lengths. 
- Space Complexity: O(N+M) since are using HashMaps of size N and M and an output array to hold our result. 