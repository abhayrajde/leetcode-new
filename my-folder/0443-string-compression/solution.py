class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            count = 1
            while i+count < len(chars) and chars[i] == chars[i+count]:
                count += 1
            print(chars[i], count)
            res = [chars[i]]
            if count > 1:
                res.extend(list(str(count)))
            chars[i:i+count] = res
            i += len(res)

        return len(chars)
        
