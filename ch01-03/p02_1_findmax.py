# 최대값 구하기
# 입력: 숫자가 n 개 들어있는 리스트
# 출력: 숫자 n개 중 최대값


def find_max(a):
	n = len(a)
	max_v = a[0]
	print("최대값 첫번째: ", max_v)

	for i in range(1, n):
		if a[i] > max_v:
			max_v = a[i]
			print("최대값 변경: ", max_v)

	return max_v


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))
