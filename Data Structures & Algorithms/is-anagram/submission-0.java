class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        // checks the lengths of strings to ensure theyre equal

        int[] store = new int[26];
        // creates an array w/ 26 spaces to represent the alphabet

        for (int i = 0; i < s.length(); i++) {
            store[s.charAt(i) - 'a']++;
            store[t.charAt(i) - 'a']--;
        }
        //loops through both strings
        //increments when looping through s 
        //decrements when looping through t
        //

        for (int n : store) if (n != 0) return false;
        //checks to see if all spaces in array equal 0
        //if a slot in the array isnt 0 thats means its not an anagram.

        return true;
    }
}

