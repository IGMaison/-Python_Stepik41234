def run(com):
    com = com.split()
    if com[0] == "pop":
        if stack:
            stack.pop()
    if com[0] == "max":
        if stack:
            print(stack[-1][1])
        else:
            print(0)
    if com[0] == "push":
        num = int(com[1])
        if stack:
            stack.append([num, max(stack[-1][1], num)])
        else:
            stack.append([num, num])


stack = []

for q in range(int(input())):
    run(input())
