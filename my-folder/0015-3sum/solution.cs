public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        IList<IList<int>> result = new List<IList<int>>();
        
        // 1. Sort the array to use the two-pointer technique
        Array.Sort(nums);
        
        for (int i = 0; i < nums.Length - 2; i++) {
            // 2. Skip duplicate values for the first number
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            // If the smallest possible sum is > 0, no need to continue
            if (nums[i] > 0) break;

            int left = i + 1;
            int right = nums.Length - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    result.Add(new List<int> { nums[i], nums[left], nums[right] });
                    
                    // 3. Skip duplicates for the second and third numbers
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++; // Sum too small, move left pointer right
                } else {
                    right--; // Sum too large, move right pointer left
                }
            }
        }
        
        return result;
    }
}
