# Add Binary

Given two binary strings a and b, return their sum as a binary string.

## Examples

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

## Constraints

Constraints:

- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.

## Approach

I initialized an empty array in order to store my resultant binary array. In order to help with the summation of the input strings, I made a helper method. Once the sum is calculated, I checked for an edge case where the sum is 0. In this instance, I just return a "0". For the fun part, we will create a for loop and divide our sum until the remainder becomes 0. After each division, if the remainder is greater than 0, I will add a "1" to the result. Once the remainder becomes 0, I just added "0"s to the end of the binary.

I had trouble with appending "O"s to the result at one point. Therefore, I created a check for the last else block. I had to make sure the result string was not empty before appending the "0". If the string was empty, that means I was appending a "0" to the beggining of the binary which was not part of the solution.

## Review & Evaluate

Time Complexity:

- input: n\*m where n and m are length of string = O(N)
- algorithm: calculating the sum for both strings O(N) + O(N) = O(N)
- while loop: O(N)
- Total = O(N) + O(N) = O(N)

Space:

- Total: O(N) because I used an extra string to store result.
