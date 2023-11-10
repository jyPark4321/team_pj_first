def plus(a,b):
  try:
    result = a + b
    return result
  except:
    print(f"더하기 에러 발생")
    return None

def minus(a,b):
  try:
    result = a - b
    return result
  except:
    print(f"빼기 에러 발생")
    return None

def multi(a,b):
  try:
    result = a * b
    return result
  except:
    print(f"곱하기 에러 발생")
    return None
#
# def Operands(infix):
#     numbers= list('01234569.')
#     recognized = []
#
#     i = 0
#     while i < len(infix):
#        j = 1
#        if infix[i] in numbers:
#          while i + j < len(infix):
#            if infix[i+j] in numbers:
#              j += 1
#            else:
#              break
#          recognized.append(''.join(infix[i:i+j]))
#          i += j
#        else:
#          recognized.append(infix[i])
#          i += 1
#     return recognized
#
# # def InToPost(infix)
# #    s = Stack()
# #    postfix = []
# #    for i in infix:
# #      if i == '(':
# #        s.push(i)
# #      else if i == ')':
# #        while s.top() != '(':
# #          postfix.append(s.pop())
# #        s.pop()
# #      else if in priority:
