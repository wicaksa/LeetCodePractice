class Solution:
    def isHappy(self, n: int) -> bool:

        # edge case where n == 0 or n == 1
        if n == 0:

            return False

        if n == 1:

            return True

        # create an empty set to keep track of the numbers we've seen
        s = set()

        # while we have not seen n in the set
        while n not in s:

            # add n to the set
            s.add(n)

            # convert n to a string
            strN = str(n)

            # create a total variable
            total = 0

            # iterate through the string
            for digit in strN:

                # calculate the total of the digits squared
                total = total + (int(digit) ** 2)

            # set n to total
            n = total

            if n == 1:

                return True

        return False
