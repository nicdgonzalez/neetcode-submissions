class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}

        for index, n in enumerate(nums):
            complement = target - n

            try:
                index_before = seen[n]
            except KeyError:
                seen[complement] = index
            else:
                return [index_before, index]
        else:
            pass

        raise Exception("every input has a pair that satisfies the condition")