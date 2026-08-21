# 0/1 Knapsack - Bottom-Up Approach

def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# 0/1 Knapsack - Top-Down Approach

def knapsack_top_down(weights, values, capacity, n, dp):

    if n == 0 or capacity == 0:
        return 0

    if dp[n][capacity] != -1:
        return dp[n][capacity]

    if weights[n - 1] <= capacity:
        dp[n][capacity] = max(
            values[n - 1] +
            knapsack_top_down(
                weights, values,
                capacity - weights[n - 1],
                n - 1, dp
            ),
            knapsack_top_down(
                weights, values,
                capacity,
                n - 1, dp
            )
        )
    else:
        dp[n][capacity] = knapsack_top_down(
            weights, values, capacity, n - 1, dp
        )

    return dp[n][capacity]


# Predefined values
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

# Bottom-Up
result1 = knapsack_bottom_up(weights, values, capacity)

# Top-Down
n = len(weights)
dp = [[-1] * (capacity + 1) for _ in range(n + 1)]

result2 = knapsack_top_down(weights, values, capacity, n, dp)

print("Maximum value using Bottom-Up:", result1)
print("Maximum value using Top-Down:", result2)
