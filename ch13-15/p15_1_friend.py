# 친구 리스트에서 자신의 모든 친구를 찾는 알고리즘
# 입력: 친구관계 그래프 g, 모든 친구를 찾을 자신 start
# 출력: 모든 친구의 이름

def print_all_friends(g, start):
	que = []
	done = set()

	que.append(start)
	done.add(start)

	while que:
		p = que.pop(0)
		print(p)

		for x in g[p]:
			if x not in done:
				que.append(x)
				done.add(x)


fr_info = {
	'Summer': ['Jhon', 'Justin', 'Mike'],
	'Jhon': ['Summer', 'Justin'],
	'Justin': ['Jhon', 'Summer', 'Mike', 'May'],
	'Mike': ['Summer', 'Justin'],
	'May': ['Justin', 'Kim'],
	'Kim': ['May'],
	'Tom': ['Jerry'],
	'Jerry': ['Tom']
}


print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')

