class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: dict[str, list[str]] = {}

        for s in strs:
            key = ''.join(sorted(s))

            try:
                existing = anagrams[key]
            except KeyError:
                # This is a new anagram.
                anagrams[key] = [s]
            else:
                # This anagram matches an existing one.
                existing.append(s)

        return list(anagrams.values())