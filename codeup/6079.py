# 언제까지 더해야할까?
a = int(input())
i=1
r=1
cnt=0
while True :
  i = i + 1
  r = r+i
  cnt += 1
  if r >= a:
    break
print(cnt+1)


