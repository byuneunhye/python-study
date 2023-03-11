# 정수 두개 입력받아 자동계산하기
a,b=map(int, input().split())
print(a+b, a-b, a*b, int(a/b), a%b, format(a/b, ".2f"), sep="\n")