# 최대값 위치 구하기
# 입력: 숫자가 n 개 들어있는 리스트
# 출력: 숫자 n개 중 최대값 위치

def find_max_idx(a):
	n = len(a)
	max_idx = 0
	print("최대값 첫번째 위치: ", max_idx)

	for i in range(1, n):
		if a[i] > a[max_idx]:
			max_idx = i
			print("최대값 위치 변경: ", max_idx)

	return max_idx

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max_idx(v))
