# 1 ~ n까지 숫자의 합 구하기 2
# 입력: n
# 출력: 1~ n까지 숫자의 합


def sum_n(n):
    return n * (n+1) // 2


print(sum_n(10))
print(sum_n(100))
