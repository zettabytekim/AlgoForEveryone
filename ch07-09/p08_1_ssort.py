# 쉬운 선택 정렬
# 입력: 리스트 a
# 출력: 정렬된 새 리스트
# 주어진 이스트에서 최소값의 위치를 돌려주는 함수


def find_min_idx(a):
	n = len(a)
	min_idx = 0
	for i in range(1, n):
		if a[i] < a[min_idx]:
			min_idx = i
	return min_idx


def sel_sort(a):
	result = []
	while a:
		min_idx = find_min_idx(a)
		value = a.pop(min_idx)
		result.append(value)
	return result


d = [2, 4, 5, 1, 3, 7, 6]
print(sel_sort(d))