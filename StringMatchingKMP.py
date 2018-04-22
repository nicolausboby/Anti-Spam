import sys

def KMP(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0]*M
    j = 0 # pattern index
    check = False

    LPS(pat, M, lps)

    i = 0 # text index
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            check = True
            print (check)
            j = lps[j-1]

        elif i < N and pat[j] != txt[i]:
            if j != 0:
                check = False
                print (check)
                j = lps[j-1]
            else:
                i += 1

def LPS(pat, M, lps):
    len = 0

    lps[0]
    i = 1

    while i < M:
        if pat[i]==pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

def main():
    teks = sys.argv[2]
    pattern = sys.argv[1]
    KMP(pattern, teks)


if __name__ == '__main__':
    main()
		


