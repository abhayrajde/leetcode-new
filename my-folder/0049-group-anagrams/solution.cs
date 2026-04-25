public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, IList<string>> dictionary = new Dictionary<string, IList<string>>();
        foreach(string str in strs) {
            char[] chars = str.ToCharArray();
            Array.Sort(chars);

            var sortedStr = new string(chars);
            if (!dictionary.ContainsKey(sortedStr)) {
                dictionary[sortedStr] = new List<string>();
            }
            dictionary[sortedStr].Add(str);
        }
        return new List<IList<string>>(dictionary.Values);
    }
}
