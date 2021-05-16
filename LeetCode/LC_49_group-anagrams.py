class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = collections.defaultdict(list)
        for word in strs:
            dict["".join(sorted(word))].append(word)
        return list(dict.values())
