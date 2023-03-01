class Solution {
    public int longestPalindrome(String s) {
        // palindrome: word that is the same backwards and forwards
        // hash map to keep track of values
        // if values are even, add it to the total
        // if values are false, subtract one
        // if there is an odd value, add 1 at the end -> put the odd value in the middle

        Map<Character, Integer> hashMap = new HashMap();
        int longestPalindrome = 0;
        boolean oddFound = false;

        // get each char and the counts into the hash map
        for (Character c : s.toCharArray()) {
            hashMap.put(c, hashMap.getOrDefault(c, 0) + 1);
        }

        for (int value : hashMap.values()) {
            if (value % 2 == 0) {
                longestPalindrome += value;
            } else {
                oddFound = true;
                longestPalindrome += value - 1;
            }
        }

        if (oddFound) {
            longestPalindrome++;
        }
        return longestPalindrome;
    }
}