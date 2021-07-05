stack = [None] * 5
top = -1

# 스택 push
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'

print('-'*5,'스텍 상태','-'*5)
for i in range(len(stack)-1,-1,-1):
    print(stack[i])

# 스택 pop

data = stack[top]
stack[top] = None
top -= 1
print(data)
