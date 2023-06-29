# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


# def gcdOfStrings(self, str1: str, str2: str) -> str:
#     # input : 2 strings
#     # output: 1 string

#     # we're checking if str2 is a substring of str2

#     result = ""

#     lenStr1 = len(str1)

#     for i in range(1, len(str2) + 1):
#         times = lenStr1 // len(str2[0:i])

#         # print(times)

#         # print(str2[0:i])

#         # print(str2[0:i] * times)

#         if str2[0:i] * times == str1:
#             result = str2[0:i]

#     return result


def gcdOfStrings(self, str1: str, str2: str) -> str:
    # input : 2 strings
    # output: 1 string

    # edge case
    if str1 == str2:
        return str1

    # get the length of each string
    len1 = len(str1)
    len2 = len(str2)

    if len1 < len2:
        # iterate backwards with the shortest string
        for i in range(len1, 0, -1):
            subString = str1[0:i]

            # if length of str1 and str2 are divisble by the current length of the substring
            if len2 % len(subString) == 0 and len1 % len(subString) == 0:
                if (
                    subString * (len2 // len(subString)) == str2
                    and subString * (len1 // len(subString)) == str1
                ):
                    return subString
    else:
        # if len2 < len1:

        # iterate backwards with the shortest string
        for i in range(len2, 0, -1):
            subString = str2[0:i]

            # if length of str1 and str2 are divisble by the current length of the substring
            if len2 % len(subString) == 0 and len1 % len(subString) == 0:
                if (
                    subString * (len2 // len(subString)) == str2
                    and subString * (len1 // len(subString)) == str1
                ):
                    return subString
    # return ""
    return ""
