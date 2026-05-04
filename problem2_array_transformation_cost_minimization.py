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
    N = int(input().strip())
    A = list(map(int, input().split()))
    K = int(input().strip())

    # Step 1: Feasibility check -- all elements must share the same remainder mod K
    r = A[0] % K
    for x in A:
        if x % K != r:
            print(-1)
            return

    # Step 2: Normalize to number-of-steps units
    # A[i] = K * B[i] + r  =>  B[i] = (A[i] - r) // K
    B = sorted((x - r) // K for x in A)

    # Step 3: Optimal target = median of B (minimizes sum of absolute deviations)
    median = B[N // 2]

    # Step 4: Sum of absolute deviations from the median
    total_ops = sum(abs(b - median) for b in B)
    print(total_ops)


# ---------------------------------------------------------------------------
# Test Cases
# ---------------------------------------------------------------------------

def run_tests():
    test_cases = [
        # (N, A, K, expected, explanation)
        (5, [2, 4, 6, 8, 10], 2,  6,  "target=6; 2+1+0+1+2=6"),
        (1, [5],              3,  0,  "single element, 0 ops"),
        (3, [6, 6, 6],        2,  0,  "all equal already, 0 ops"),
        (3, [1, 2, 3],        2, -1,  "1%2=1, 2%2=0 -> impossible"),
        (4, [0, 2, 4, 6],     2,  4,  "B=[0,1,2,3], median=1 or 2, cost=4"),
        (3, [1, 3, 5],        2,  2,  "B=[0,1,2], median=1, cost=1+0+1=2"),
        (2, [10, 20],         5,  2,  "B=[2,4], median=4, cost=2; or median=2, cost=2"),
        (5, [1, 1, 1, 1, 1],  5,  0,  "all same"),
        (3, [3, 6, 9],        3,  2,  "B=[1,2,3], median=2, cost=1+0+1=2"),
        (4, [5, 3, 1, 7],     2, -1,  "5%2=1, 3%2=1, 1%2=1, 7%2=1 -> feasible; "
                                       "B=[0,1,2,3], median=B[2]=2, cost=2+1+0+1=4. "
                                       "Wait: 5//2=2,3//2=1,1//2=0,7//2=3 sorted=[0,1,2,3]"
                                       " median=B[2]=2, cost=2+1+0+1=4. Expected=-1 is wrong."
                                       " Correcting expected to 4"),
    ]

    # Fix test 10 expected value (was placeholder -1, actual is 4)
    test_cases[9] = (4, [5, 3, 1, 7], 2, 4, "5%2=3%2=1%2=7%2=1; B=[0,1,2,3], median=2, cost=2+1+0+1=4")

    print("Running test cases...\n")
    all_passed = True

    for i, (n, a, k, expected, explanation) in enumerate(test_cases):
        # Run the algorithm inline
        r = a[0] % k
        feasible = all(x % k == r for x in a)

        if not feasible:
            result = -1
        else:
            B = sorted((x - r) // k for x in a)
            median = B[n // 2]
            result = sum(abs(b - median) for b in B)

        status = "[PASS]" if result == expected else "[FAIL] got={}, expected={}".format(result, expected)
        if result != expected:
            all_passed = False
        print("Test {:2d}: N={}, A={}, K={} | {}".format(i + 1, n, a, k, status))
        print("         {}\n".format(explanation))

    print("=" * 60)
    print("All tests passed!" if all_passed else "Some tests FAILED!")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        solve()
