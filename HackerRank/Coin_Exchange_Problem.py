def getMaximumWays(n, coin_list):
    coin_list.sort()
    length = len(coin_list)
    table = {}
    for i in range(0, length):
        table[i, 0] = 1

    for j in range(1, n + 1):
        if j % coin_list[0] == 0:
            table[0, j] = 1
        else:
            table[0, j] = 0

    for i in range(1, length):
        for j in range(1, n + 1):
            if j < coin_list[i]:
                table[i, j] = table[i - 1, j]
            else:
                table[i, j] = table[i - 1, j] + table[i, j - coin_list[i]]

    return table[length - 1, n]
