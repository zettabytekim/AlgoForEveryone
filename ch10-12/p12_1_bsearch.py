# 리스트에서 특정 숫자 위치 찾기(이분 탐색)
# 입력: 리스트 a, 찾는 값 x
# 출력: 찾으면 그 값의 위치, 찾지 못하면 -1


def binary_search(a, x):
 	start = 0
 	end = len(a) - 1

 	while start <= end:
 		mid = (start+end) // 2
 		if x == a[mid]:
 			return mid
 		elif x > a[mid]:
 			start = mid + 1
 		else:
 			end = mid - 1


 	return -1

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))
