# 정수 3개 입력받아 가장 작은 값 출력하기
a, b, c = input().split()
a=int(a)
b=int(b)
c=int(c)
print((a if(a<=b) else b)if b<=c else c)
