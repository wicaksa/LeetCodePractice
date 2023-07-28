def productExceptSelf(self, nums: List[int]) -> List[int]:
    N = len(nums)
    result = [1] * N

    factor = 1

    for i in range(0, N):
        result[i] *= factor

        factor *= nums[i]

    # print(result)

    factor = 1

    for i in range(N - 1, -1, -1):
        result[i] *= factor

        factor *= nums[i]

    # print(result)

    return result
