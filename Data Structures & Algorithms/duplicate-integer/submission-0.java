class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> checked = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (checked.contains(nums[i]))
                return true;
            checked.add(nums[i]);
        }
        return false;
}
}