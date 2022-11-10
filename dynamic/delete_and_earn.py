from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        num_value = {}
        for n in nums:
            num_value[n] = num_value.get(n, 0) + n

        dp_number = []
        dp_value = []

        i = 0
        sorted_nums = sorted(num_value.keys())
        for n in sorted_nums:
            dp_number.append(n)
            dp_value.append(num_value[n])

            if i > 0:
                previous_n = dp_number[i-1]
                if n-1 == previous_n:
                    if i > 1:
                        dp_value[i] = max(dp_value[i-1], num_value[n]+dp_value[-3])
                    else:
                        dp_value[i] = max(num_value[previous_n], num_value[n])
                else:
                    dp_value[i] = dp_value[i-1]+num_value[n]

            i += 1

        return dp_value[-1]
