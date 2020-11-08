def find_longest_substring(text1, text2):
    len1 = len(text1)
    len2 = len(text2)

    substring_count = {}
    largest = 0
    largest_substring_end = -1
    for i in range(0, len1):
        for j in range(0, len2):
            if text1[i] == text2[j]:
                if i == 0 or j == 0:
                    substring_count[(i, j)] = 1
                else:
                    substring_count[(i, j)] = 1 + substring_count[(i - 1, j - 1)]
                    if largest < substring_count[(i, j)]:
                        largest=substring_count[(i,j)]
                        largest_substring_end=(i,j)
            else:
                substring_count[(i, j)] = 0

    if largest > 0:
        return text1[largest_substring_end[0]-largest+1:largest_substring_end[0]+1]
    else:
        return None


longest_common_substring = find_longest_substring("abcdkf", "abcldkf")
print(longest_common_substring)
