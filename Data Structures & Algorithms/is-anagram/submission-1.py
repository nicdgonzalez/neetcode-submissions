class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Letters cannot be added or removed.
        if len(s) != len(t):
            return False

        s_counted = [(c, s.count(c)) for c in set(s)]
        s_counted.sort()

        t_counted = [(c, t.count(c)) for c in set(t)]
        t_counted.sort()

        return s_counted == t_counted