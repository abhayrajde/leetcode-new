public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        foreach(int ele in nums) {
            if (!dict.ContainsKey(ele)) {
                dict[ele] = 1;
            }
            dict[ele] += 1;
        }
        var sortedPairs = dict.OrderByDescending(x => x.Value);
        var TopKKeys = sortedPairs.Take(k).Select(x => x.Key).ToArray();
        return TopKKeys;
    }
}
