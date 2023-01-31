## About

This section focused on searching for an item in a array. There are two methods presented in this section, the linear search and the binary search.

# Linear Search

This algorithm focuses on searching an array for a target item one by one until the end of the array. Usually, edge cases are handled first.
The common edge cases for this search is seeing if the array is null or if you can't find the target in the array. Because of the second edge case,
the time complexity for this search is O(N).

# Binary Search

This algorithm focuses on finding the midpoint of the array and searching if the target is to the left or the right of the element in the midpoint.
Since each iteration cuts the search by half, this method is faster than the linear search.
