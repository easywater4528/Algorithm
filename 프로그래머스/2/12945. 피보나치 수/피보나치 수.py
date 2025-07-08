MOD = 1234567

def solution(n: int) -> int:
    a, b = 0, 1          # F(0), F(1)
    for _ in range(n):   # n ≤ 100 000 ⇒ 약 0.04 ms
        a, b = b, (a + b) % MOD
    return a
