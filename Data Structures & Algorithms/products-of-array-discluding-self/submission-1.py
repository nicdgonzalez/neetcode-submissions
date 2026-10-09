import math
import itertools


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        values = []

        is_positive = nums.count(-1) % 2 == 0
        precomputed_product = math.prod(nums)

        for i in range(len(nums)):
            if nums[i] == 1:
                # Product is the same as if this value was not excluded.
                values.append(precomputed_product)
            elif nums[i] == -1:
                # If count for -1 was even, now it's odd, so flip the boolean.
                values.append(precomputed_product * -1)
            else:
                before = list(filter(lambda n: abs(n) != 1, nums[:i]))
                after = list(filter(lambda n: abs(n) != 1, nums[i + 1:]))
                value = math.prod([*before, *after]) * (1 if is_positive else -1)
                values.append(value)


        return values