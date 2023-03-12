# 정수 두개 입력받아서 하나라도 참이면 참 출력하기
a,b = input().split()
print(bool(int(a)) or bool(int(b)))
