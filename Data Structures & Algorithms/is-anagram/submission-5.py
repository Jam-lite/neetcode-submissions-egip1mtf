class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        char_freq_s, char_freq_t = {}, {}

        for char in s:
           char_freq_s[char] = 1 + char_freq_s.get(char, 0)
        
        for char in t:
           char_freq_t[char] = 1 + char_freq_t.get(char, 0)

        if char_freq_s == char_freq_t:
            return True
        return False
