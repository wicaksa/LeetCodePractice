def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    result = []

    maxValue = max(candies)

    for candy in candies:
        if candy + extraCandies >= maxValue:
            result.append(True)

        else:
            result.append(False)

    return result
