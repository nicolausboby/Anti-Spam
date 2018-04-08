class LastOccurrence(object):
    def __init__(self, pattern, alphabet):
        self.occurrences = dict()
        for letter in alphabet:
            self.occurrences[letter] = pattern.rfind(letter)

    def __call__(self, letter):
        return self.occurrences[letter]


def boyer_moore_matching(text, pattern):
    alphabet = set(text)
    last = LastOccurrence(pattern, alphabet)
    m = len(pattern)
    n = len(text)
    i = m - 1  # text index
    j = m - 1  # pattern index
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last(text[i])
            i = i + m - min(j, 1 + l)
            j = m - 1
    return -1


def main():
    sample = open("sample.txt", "r")
    sample_string = sample.read()
    spam_pattern = "aaab"
    found = boyer_moore_matching(sample_string, spam_pattern)
    if found == -1:
        print("no match found!")
    else:
        print("found match on : ", len(sample_string)-(found+len(spam_pattern))+1, "-", len(sample_string)-found+1)


if __name__ == "__main__":
    main()