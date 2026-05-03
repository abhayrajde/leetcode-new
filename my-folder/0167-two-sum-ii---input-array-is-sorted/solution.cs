public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int l = 0, r = numbers.Length - 1;
        int[] res = Array.Empty<int>();
        while (l < r) {
            if (numbers[l] + numbers[r] == target) {
                res = new int[]{l + 1, r + 1};
                break;
            } else if(numbers[l] + numbers[r] < target) {
                l += 1;
            } else {
                r -= 1;
            }
        } 
        return res;      
    }
}
