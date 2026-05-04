"""
Problem 1: Cyclic Substring Maximum Sum
========================================
Given a string S of lowercase English alphabets, each character has a value
equal to its position in the alphabet (a=1, b=2, ..., z=26).

Find the maximum possible sum of character values from any cyclic substring
such that no character appears more than once in the chosen substring.

Approach:
---------
1. A cyclic substring can wrap from end to beginning.
   To handle this, we double the string: T = S + S.
   Any cyclic substring of S corresponds to a contiguous substring in T
   with length <= len(S).

2. Use a sliding window (two-pointer technique) on T:
   - Expand the right pointer and add the character.
   - If a duplicate is found, shrink the left pointer until the duplicate
     is removed.
   - Also ensure the window size never exceeds len(S).
   - Track the maximum sum at each step.

Time Complexity:  O(n)  -- each character enters/exits the window at most once
Space Complexity: O(1)  -- at most 26 characters in the frequency map
"""


def solve():
    s = input().strip()
    n = len(s)

    if n == 0:
        print(0)
        return

    t = s + s
    freq = {}
    left = 0
    curr = 0
    ans = 0

    for right in range(len(t)):
        ch = t[right]
        val = ord(ch) - ord('a') + 1

        while freq.get(ch, 0) > 0 or (right - left + 1) > n:
            left_ch = t[left]
            freq[left_ch] -= 1
            curr -= ord(left_ch) - ord('a') + 1
            left += 1

        freq[ch] = freq.get(ch, 0) + 1
        curr += val
        ans = max(ans, curr)

    print(ans)


if __name__ == "__main__":
    solve()
