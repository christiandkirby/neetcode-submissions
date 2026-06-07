class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int num : nums){
            if (hm.containsKey(num)){
                return true;
            }
            if (!hm.containsKey(num)){
                hm.putIfAbsent(num, 0);
            }
        }
        return false;
        
    }
}
