class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts: dict[int, int] = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        counts_sorted = sorted(
            counts.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [item[0] for item in counts_sorted][:k]
