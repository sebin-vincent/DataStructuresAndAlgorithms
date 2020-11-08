def createLPSchart(pattern):
    occurrence_map = {}
    lpsMap = {}
    length = len(pattern)
    for i in range(0, length):
        if pattern[i] not in occurrence_map:
            occurrence_map[pattern[i]] = 0
            lpsMap[i] = -1
        else:
            lpsMap[i] = lpsMap[i - 1] + 1
    return lpsMap


def findCommonSubstring(text, pattern):
    lpsChart = createLPSchart(pattern)
    lpsChart[-1] = -1

    j = -1
    n = len(text)
    endOfPattern = len(pattern) - 1
    for i in range(0, n):
        if pattern[j + 1] == text[i]:
            j = j + 1
            if j == endOfPattern:
                return i - j
        else:
            j = lpsChart[j + 1]


text = "ababcabcabababd"
pattern = "ababd"
print(findCommonSubstring(text, pattern))
