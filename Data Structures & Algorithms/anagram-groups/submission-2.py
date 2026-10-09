class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: dict[str, list[str]] = {}

        for s in strs:
            key = ''.join(sorted(s))
            anagrams.setdefault(key, []).append(s)

        return list(anagrams.values())