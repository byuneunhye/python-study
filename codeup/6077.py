# 짝수 합 구하기
a = int(input())
r=0
for i in range(1, a+1):
  if i %2==0:
    r = r+i
print(r)