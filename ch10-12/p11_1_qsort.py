# 쉽게 설명한 퀵 정렬
# 입력: 리스트 a
# 출력: 정렬된 새 리스트


def quick_sort(a):
	n = len(a)
	if n <= 1:
		return a

	pivot = a[-1]	# 임의로 마지막 값을 기준값으로 하였음
	g1 = []
	g2 = []

	for i in range(0, n-1):
		if a[i] < pivot:
			g1.append(a[i])
		else:
			g2.append(a[i])


	return quick_sort(g1) + [pivot] + quick_sort(g2)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))
