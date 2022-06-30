class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        let_dict = {}
        for i in s:
            if i not in let_dict.keys():
                let_dict[i] = 1
            else:
                let_dict[i] += 1
                if let_dict[i] % 2 == 0:
                    longest += let_dict[i]
                    let_dict[i] = 0
        
        if any(let_dict.values()):
            return longest + 1
        else:
            return longest
        
        