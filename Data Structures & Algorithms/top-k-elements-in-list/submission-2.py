from typing import NamedTuple

class Counted(NamedTuple):
    number: int
    count: int


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        start = 0
        current = 1

        counts: list[Counted] = []

        while start < len(nums):
            number = nums[start]

            while current < len(nums) and nums[current] == number:
                current += 1

            count = current - start
            counts.append(Counted(number=number, count=count))

            start = current

        counts.sort(key=lambda c: c.count, reverse=True)

        return [c.number for c in counts][:k]