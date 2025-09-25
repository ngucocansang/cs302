"""
a.
1. Most valuable first (values desc): 6 → 5 → 4 → 3 → 2 → 1
- Picked: 6,5,1
- Total weight = 9 + 7 + 2 = 18
- Total value = 28+25 +7 = 60

2. Lightest first (weights asc): 1 → 2 → 3 → 4 → 5 → 6
- Picked: 1, 2, 3, 4
- Total weight = 2 + 3 + 5 + 6 = 16
- Total value = 7 + 11 + 18 + 22 = 58

3. Best value/weight ratio (desc): items sorted ≈ [2, 4, 3, 5, 1, 6]
- Picked: 2, 4, 3, 1
- Total weight = 3 + 6 + 5 + 2 = 16
- Total value = 11 + 22 + 18 + 7 = 58

Greedy answers: values = 60, 58, 58 respectively. Note greedy is not guaranteed optimal.


b. Dynamic programming (0/1 knapsack) — table and optimal value 
I filled the DP table V[i][w] (i = 0..6 items, w = 0..18 capacity).

The final row (using all 6 items) gives the maximum values for capacities 0..18:
-) V[6][0..18] = [0,0,7,11,11,18,22,25,29,33,36,40,43,47,51,54,58,61,65]

So the maximum possible value for capacity 18 is:
- Optimal value = 65 (i.e. V[6][18] = 65).

c. Recovering the optimal item set (backtracking)
Start from i = 6, w = 18 and compare V[i][w] with V[i-1][w]:
- Doing this gives the chosen items: {1, 2, 4, 5} (items by their indexes).

Check:
- weights = 2 + 3 + 6 + 7 = 18 (fits capacity)
- values = 7 + 11 + 22 + 25 = 65 (the optimal value)

So the optimal selection is items 1, 2, 4, 5 with total value 65 and total weight 18.
"""