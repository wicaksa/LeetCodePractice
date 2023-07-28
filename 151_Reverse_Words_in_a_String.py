def reverseWords(self, s: str) -> str:
    # Input : string s -> separated by at least 1 space
    #                  -> may contain leading or trailing spaces or multiple spaces b/w words
    # Output: string t -> separated by one space

    output = ""

    currentWord = ""

    for char in s.strip():
        if char.isalnum():
            currentWord += char

        if char == " ":
            if len(currentWord) != 0:
                output = " " + currentWord + output

                currentWord = ""

    return currentWord + output
