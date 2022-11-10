class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total_product = 1
        total_product_wo_zero = 1
        result = []
        count_zero = 0

        for n in nums:
            total_product *= n
            if n == 0:
                count_zero += 1
            else:
                total_product_wo_zero *= n

        for n in nums:
            if n == 0:
                if count_zero == 1:
                    result.append(int(total_product_wo_zero))
                else:
                    result.append(0)
            else:
                result.append(int(total_product/n))

        return result
