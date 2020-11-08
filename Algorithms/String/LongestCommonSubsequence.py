def get_longest_common_subsequence(text1, text2):
    len1 = len(text1)
    len2 = len(text2)

    largest = 0
    count_map = {}
    largest_sequence_endpoint = (0, 0)
    for i in range(0, len1 + 1):
        for j in range(0, len2 + 1):
            if i == 0 or j == 0:
                count_map[(i, j)] = 0
                continue
            elif text1[i - 1] == text2[j - 1]:
                count_map[(i, j)] = 1 + count_map[(i - 1, j - 1)]
                largest = count_map[(i, j)]
                largest_sequence_endpoint = (i, j)
            else:
                count_map[(i, j)] = count_map[(i - 1, j)] if count_map[(i - 1, j)] >= count_map[(i, j - 1)] else \
                    count_map[(i, j - 1)]

    subsequence = ""
    i, j = largest_sequence_endpoint
    if largest:
        while count_map[(i, j)] != 0:
            path = (i - 1, j) if (count_map[(i - 1, j)]) >= count_map[(i, j - 1)] else (i, j - 1)
            if count_map[path] != count_map[i, j]:
                subsequence = text1[i - 1] + subsequence
                i = i - 1
                j = j - 1
            else:
                i, j = path

        return subsequence
    else:
        return None


text1 = "stone"
text2 = "longest"

longest_subsequence = get_longest_common_subsequence(text1, text2)

print(longest_subsequence)
