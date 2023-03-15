# 정수 1개 입력받아 분류하기
a = input()
a=int(a)

if (a<0) and (a%2==0):
  print("A")

if (a<0) and (a%2!=0):
  print("B")

if (a>0) and (a%2==0):
  print("C")

if (a>0) and (a%2!=0):
  print("D")






