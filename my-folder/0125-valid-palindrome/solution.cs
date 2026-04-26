public class Solution {
    public bool IsPalindrome(string s) {
        string cleanString = new string(s.Where(char.IsLetterOrDigit)
                                        .Select(char.ToLower)
                                        .ToArray());
        
        Console.WriteLine(cleanString);
        return cleanString == new string(cleanString.Reverse().ToArray());
    }
}
