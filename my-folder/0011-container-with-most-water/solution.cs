public class Solution {
    public int MaxArea(int[] height) {
        int res = 0;
        int l = 0, r = height.Length - 1;
        while (l < r) {
            int area = Math.Min(height[l], height[r]) * (r - l);
            res = Math.Max(res, area);
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return res;
    }
}
