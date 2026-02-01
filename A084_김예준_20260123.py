s = input()
suffixes = [s[i:] for i in range(len(s))]
suffixes.sort()

for suf in suffixes:
    print(suf)
