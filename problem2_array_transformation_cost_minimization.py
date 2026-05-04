"""
Problem 2: Array Transformation Cost Minimization
===================================================
Given array A of size N and a fixed integer K. We can add or subtract K
from any element any number of times.
Goal: make all elements equal with minimum total operations, or -1 if impossible.

Key Observations:
-----------------
1. A[i] can only reach values: A[i], A[i]+K, A[i]-K, A[i]+2K, ...
   i.e., any value of the form  A[i] + m*K  for integer m.

2. Two elements A[i] and A[j] can reach the same value only if:
   (A[i] - A[j]) is divisible by K  =>  A[i] % K == A[j] % K
   If any element has a different remainder, return -1.

3. If feasible, normalize: B[i] = (A[i] - r) // K
   Cost to bring B[i] to target t  =  |B[i] - t|  (each step covers K).
   Total cost = sum of |B[i] - t|, minimized when t = median(B).

Time Complexity:  O(N log N)  -- dominated by sorting for the median
Space Complexity: O(N)
"""

def solve():
    n = int(input().strip())
    a = list(map(int, input().split()))
    k = int(input().strip())

    r = a[0] % k

    for x in a:
        if x % k != r:
            print(-1)
            return

    b = sorted((x - r) // k for x in a)
    median = b[n // 2]

    ans = sum(abs(x - median) for x in b)
    print(ans)


if __name__ == "__main__":
    solve()
