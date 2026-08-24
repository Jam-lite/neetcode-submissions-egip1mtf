class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a .. z

            for c in s:
                count[ord(c) - ord("a")] += 1

            # Lists cannot be dictionary keys, so convert count to a tuple
            result[tuple(count)].append(s)
        
        return list(result.values())