# 문자 1개 입력받아 알파벳 출력하기
e = ord(input())
a = ord('a')
while e >= a:
  print(chr(a), end = ' ')
  a += 1