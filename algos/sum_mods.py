# Given an array of integers A. 
# Calculate the sum of A[i] %A[j] for all possible i,j pair. 
# return sum%(10^9+7) as an output.
# Solve this problem on o(n).
arr = {1,2,3}
max_num = max(arr)
counter = {}
for i in arr:
    counter[i] = counter.get(i, 0) + 1
total = 0
mod = 10 ** 9 + 7
for i in range(1, max_num + 1):
    for j in range(1, max_num + 1):
        total += counter[i] * counter[j] * (i % j)
        total %= mod
# (x + y) % n = ((x % n) + (y % n)) % n
# (a + b + c) % n = ((a % n) + (b % n) + (c % n)) % n
print(total)

