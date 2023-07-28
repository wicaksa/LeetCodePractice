class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # edge case when flowerbed is [0]

        if flowerbed == [0]:
            return n == 1 or n == 0

        if flowerbed == [1]:
            return n == 0

        for i in range(0, len(flowerbed)):
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and n >= 1:
                    flowerbed[i] = 1

                    n = n - 1

            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and n >= 1:
                    flowerbed[i] = 1

                    n = n - 1

            else:
                if (
                    flowerbed[i] == 0
                    and flowerbed[i - 1] == 0
                    and flowerbed[i + 1] == 0
                    and n >= 1
                ):
                    flowerbed[i] = 1

                    n = n - 1

            print(n)

            if n == 0:
                return True

        return False
