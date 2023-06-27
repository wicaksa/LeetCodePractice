# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


def gcdOfStrings(self, str1: str, str2: str) -> str:
    # input : 2 strings
    # output: 1 string

    # we're checking if str2 is a substring of str2

    result = ""

    lenStr1 = len(str1)

    for i in range(1, len(str2) + 1):
        times = lenStr1 // len(str2[0:i])

        # print(times)

        # print(str2[0:i])

        # print(str2[0:i] * times)

        if str2[0:i] * times == str1:
            result = str2[0:i]

    return result
