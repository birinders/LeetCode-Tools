import pickle

with open("tools/intermediate_d", "rb") as handle:
    d = pickle.load(handle)

# Assuming everything is stored in (row, column) format


def get_arr_wo_None(d):
    height = (
        max(d.keys(), key=lambda x: x[0])[0] - min(d.keys(), key=lambda x: x[0])[0] + 1
    )
    # Accounting for None
    # height += 1

    width = (
        max(d.keys(), key=lambda x: x[1])[1] - min(d.keys(), key=lambda x: x[1])[1] + 1
    )

    dp = [[0] * width for _ in range(height)]

    for (y, x), val in d.items():
        if y == None:
            y = 0
        else:
            y = y + 1
        dp[y][x] = val

    return dp


# print(*dp, sep="\n")
