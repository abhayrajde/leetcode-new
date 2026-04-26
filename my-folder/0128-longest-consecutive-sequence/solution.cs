public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> numSet = new (nums);
        int longest = 0;
        foreach(int ele in numSet) {
            if (!numSet.Contains(ele - 1)) {
                int length = 1;

                while (numSet.Contains(ele + length)) {
                    length += 1;
                }
                longest = Math.Max(longest, length);
            }
        }
        return longest;
    }
}
