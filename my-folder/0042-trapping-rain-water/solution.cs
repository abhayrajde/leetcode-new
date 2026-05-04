public class Solution {
    public int Trap(int[] height) {
        int l = 0, r = height.Length - 1;
        int leftMax = height[l], rightMax = height[r];
        int water = 0;

        while(l < r) {
            if (leftMax < rightMax) {
                l++;
                leftMax = Math.Max(leftMax, height[l]);
                water += leftMax - height[l];
            } else {
                r--;
                rightMax = Math.Max(rightMax, height[r]);
                water += rightMax - height[r];
            }
        }
        return water;
    }
}
