public class Solution {
    public bool IsPalindrome(string s) {
        string result = "";
        foreach(char c in s) {
            if (char.IsLetterOrDigit(c)) {
                result += char.ToLower(c);
            }
        }

        return (result == new string(result.Reverse().ToArray()));
    }
}
