# 주어진 문장이 회문인지 아닌지 찾기(큐와 스택의 특징을 이용)
# 입력: 문자열 s
# 출력: 회문이면 True, 아니면 False


def palindrome(s):
	que = []
	stk = []

	for x in s:
		if x.isalpha():
			que.append(x.lower())
			stk.append(x.lower())

	while que:
		if que.pop(0) != stk.pop():
			return False

	return True


print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam"))
print(palindrome("Madam, I am Adam"))