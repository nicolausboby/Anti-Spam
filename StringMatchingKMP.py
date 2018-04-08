def KMP(pattern, text):
	np = len(pattern)
	nt = len(text)

	longest = [0] * np
	pi = 0

	PrefixSufix(pattern, np, longest)

	i = 0
	while (i < nt):
		if (pattern[pi] == text[i]):
			i += 1
			pi += 1

		if (pi == np):
			print("It's a Spam")
			pi = longest[pi-1]

		elif (i < nt) and (pattern[pi] != text[i]):
			if (pi != 0):
				pi = longest[pi-1]
			else:
				i += 1

def PrefixSufix(pattern, np, longest):
	len = 0
	longest[0]
	i = 1

	while (i < np):
		if (pattern[i] == pattern[len]):
			len += 1
			longest = len
			i += 1
		else:
			if (len != 0):
				len = longest[len-1]
			else:
				longest[i] = 0
				i += 1

def main():
	text = "ABCDEFGHIJ"
	pattern = "CDEFG"
	KMP(pattern, text)

if __name__ == '__main__':
	main()
		


