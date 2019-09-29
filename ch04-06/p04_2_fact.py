# 연속한 숫자의 곱을 구하는 알고리즘연 2
# 입력: n
# 출력: 1부터 n까지 연속한 숫자를 곱합 값


def fact(n):
	if n <= 1:
		return 1
	return n * fact(n-1)


print(fact(1))
print(fact(5))
print(fact(10))
