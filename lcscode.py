def lcsRec_py(s1, s2, m, n, memo):
    # Base Case
    if m == 0 or n == 0:
        return 0
 
    # Already exists in the memo table
    if memo[m][n] != -1:
        return memo[m][n]

    # Match
    if s1[m - 1] == s2[n - 1]:
        memo[m][n] = 1 + lcsRec_py(s1, s2, m - 1, n - 1, memo)
        return memo[m][n]

    # Do not match
    memo[m][n] = max(lcsRec_py(s1, s2, m, n - 1, memo),lcsRec_py(s1, s2, m - 1, n, memo))
    return memo[m][n]

def lcs_py(s1, s2):
    m = len(s1)
    n = len(s2)
    # Initialize memoization table with -1
    memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

    return lcsRec_py(s1, s2, m, n, memo)

# driver code
s1_py = "AGGTAB"
s2_py = "GXTXAYB"

print(f"LCS length for '{s1_py}' and '{s2_py}': {lcs_py(s1_py, s2_py)}")