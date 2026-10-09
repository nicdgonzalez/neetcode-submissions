# Byte order choice is arbitrary.
# As long as the encoder and decoder are in agreement, either one works.
BYTE_ORDER = "little"


class Solution:

    def encode(self, strs: List[str]) -> str:
        # Strings are a collection of bytes. Each byte contains a numerical value
        # between 0 and 255. Because all strings are guaranteed to be 200 bytes or less,
        # we can prepend the length (NOTE: as a single byte) to each of the strings
        # and then concatenate them.
        encoded = ""
        
        for s in strs:
            assert 0 <= len(s) <= 200
            encoded += f"{len(s):0>3}"
            encoded += s

        return encoded

    def decode(self, s: str) -> List[str]:
        strs: list[str] = []

        # Represents a "slice" of data.
        start = 0

        while start < len(s):
            end = start + 3
            length = int(s[start:end])
            start = end

            end = start + length
            string = s[start: end]
            strs.append(string)
            start = end

        return strs