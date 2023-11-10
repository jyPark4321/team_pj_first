import calc

print("연동 테스트파일입니다.")

print("입력 예 : 2x6,2+4,(2+4)*2")
a = int(input())
b = int(input())
c = calc.plus(a,b)
d = calc.minus(a,b)
f = calc.multi(a,b)
print(c,d,f)


