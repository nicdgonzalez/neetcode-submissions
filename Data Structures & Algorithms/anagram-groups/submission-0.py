from typing import NamedTuple, Iterable


class WithCount[T](NamedTuple):
    element: T
    count: int

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        
        return (self.element, self.count) == (other.element, other.count)

    def __hash__(self) -> int:
        return hash((self.element, self.count))


# NOTE: The order of returned counts are not guaranteed.
def with_counts[T](collection: Iterable[T]) -> list[WithCount[T]]:
    # Remove duplicates to avoid counting the same element multiple times.
    # e.g., `aaa` becomes `[a: 3]` instead of `[a: 3, a: 3, a: 3]`.
    unique_elements = set(collection)

    return [
        WithCount(
            element=element,
            count=sum(1 for x in collection if x == element)
        )
        for element in unique_elements
    ]


class Counted[T]:
    def __init__(self, collection: Iterable[T], /) -> None:
        counts = with_counts(collection)
        # Sort once immediately after counting to avoid creating sorted copies
        # for each `hash` and/or equality check.
        counts.sort(key=lambda e: e.element)

        self.counts = counts

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        
        return tuple(self.counts) == tuple(other.counts)

    def __hash__(self) -> int:
        value = 0

        for count in self.counts:
            value += hash(count)

        return value


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: dict[Counted[str], list[str]] = {}

        for s in strs:
            counts = Counted(s)

            try:
                existing = anagrams[counts]
            except KeyError:
                # This is a new anagram.
                anagrams[counts] = [s]
            else:
                # This anagram matches an existing one.
                existing.append(s)

        return [v for k, v in anagrams.items()]