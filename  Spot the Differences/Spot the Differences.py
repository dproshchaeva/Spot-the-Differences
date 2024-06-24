def spot_diff(s1, s2):
    return [i for i in range(len(s1)) if s1[i] != s2[i]]


s1 = "abcdefg"
s2 = "abcqetg"
result = spot_diff(s1, s2)
print(result)