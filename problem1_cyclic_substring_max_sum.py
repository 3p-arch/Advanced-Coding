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
    S = input().strip()
    n = len(S)

    if n == 0:
        print(0)
        return

    # Double the string to handle cyclic substrings
    T = S + S

    char_count = {}   # frequency of each character in current window
    current_sum = 0   # sum of values in current window
    max_sum = 0       # answer
    left = 0          # left pointer of the sliding window

    for right in range(len(T)):
        ch = T[right]
        val = ord(ch) - ord('a') + 1  # a=1, b=2, ..., z=26

        # Shrink window if this character is already in the window (duplicate)
        while char_count.get(ch, 0) > 0:
            left_ch = T[left]
            char_count[left_ch] -= 1
            current_sum -= ord(left_ch) - ord('a') + 1
            left += 1

        # Shrink window if its size would exceed n (can't use full string twice)
        while (right - left + 1) > n:
            left_ch = T[left]
            char_count[left_ch] -= 1
            current_sum -= ord(left_ch) - ord('a') + 1
            left += 1

        # Add current character to the window
        char_count[ch] = char_count.get(ch, 0) + 1
        current_sum += val

        # Update maximum sum
        if current_sum > max_sum:
            max_sum = current_sum

    print(max_sum)


# ---------------------------------------------------------------------------
# Test Cases
# ---------------------------------------------------------------------------

def run_tests():
    test_cases = [
        # (input_string, expected_output, explanation)
        ("abca",   6,  "abc/bca/cab all give sum 6; 'abca' has dup 'a'"),
        ("a",      1,  "single character: a=1"),
        ("z",     26,  "single character: z=26"),
        ("abcde", 15,  "all unique, full string: 1+2+3+4+5=15"),
        ("aaa",    1,  "all same; only window of size 1 is valid, a=1"),
        ("zy",    51,  "z=26 + y=25 = 51"),
        ("abcba",  6,  "abc=6, cba=6; wrapping gives dups; max=6"),
        ("abcabc", 6,  "abc=6 is the longest unique cyclic substring"),
        ("xyz",   75,  "x=24 + y=25 + z=26 = 75"),
        ("ba",     3,  "b=2 + a=1 = 3"),
        ("dcba",  10,  "d=4 + c=3 + b=2 + a=1 = 10"),
    ]

    print("Running test cases...\n")
    all_passed = True

    for i, (s, expected, explanation) in enumerate(test_cases):
        n = len(s)
        T = s + s
        char_count = {}
        current_sum = 0
        max_sum = 0
        left = 0

        for right in range(len(T)):
            ch = T[right]
            val = ord(ch) - ord('a') + 1
            while char_count.get(ch, 0) > 0:
                lc = T[left]
                char_count[lc] -= 1
                current_sum -= ord(lc) - ord('a') + 1
                left += 1
            while (right - left + 1) > n:
                lc = T[left]
                char_count[lc] -= 1
                current_sum -= ord(lc) - ord('a') + 1
                left += 1
            char_count[ch] = char_count.get(ch, 0) + 1
            current_sum += val
            if current_sum > max_sum:
                max_sum = current_sum

        status = "[PASS]" if max_sum == expected else "[FAIL] got={}, expected={}".format(max_sum, expected)
        if max_sum != expected:
            all_passed = False
        print("Test {:2d}: S='{}' | {}".format(i + 1, s, status))
        print("         {}\n".format(explanation))

    print("=" * 60)
    print("All tests passed!" if all_passed else "Some tests FAILED!")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        solve()