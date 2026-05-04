public class Solution {
    public int LengthOfLongestSubstring(string s) {
        HashSet<int> set = new HashSet<int>();
        int l = 0, r = 0;
        int res = 0;
        // set.Add(s[0]);
        while (r < s.Length) {
            if (set.Contains(s[r])) {
                set.Remove(s[l]);
                l++;
                // while(set.Contains(s[r])) {
                // }
            } else {
                set.Add(s[r]);
                res = Math.Max(res, r-l+1);
                r ++;
            }
        }
        return res;
    }
}
