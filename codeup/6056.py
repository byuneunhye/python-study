# 참/거짓이 서로 다를때에만 참 출력하기
a,b = input().split()
a=bool(int(a))
b=bool(int(b))
print(a and (not b) or b and (not a))

# 처음에 
# a,b = bool(input().split())
# print(a and (not b) or b and (not a))
# 으로 작성하였는데 오류가 났다.
# 이유는 bool() 함수에 input().split()을 전달하고 있어서였다.
# input() 함수는 사용자에게 입력을 받는 함수,
# split() 함수는 문자열을 공백을 기준으로 분리한 리스트를 반환,
# bool() 함수는 문자열 리스트를 입력으로 받게되며 이는 항상 "True"를 반환한다.
# 따라서 빈문자열: False
# 그 외: True
# 그래서 a,b = bool(input().split()) 이 코드에는 항상 True가 반환된다.