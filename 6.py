n, lst, w = int(input()), [int(i) for i in input().split()], int(input())
que = [0]
for i in range(n):
    if i >= w and que[0] == lst[i-w]:
        que.pop(0)
    while que and que[-1] < lst[i]:
        que.pop()
    que.append(lst[i])
    if i+1 >= w:
        print(que[0],end=' ')