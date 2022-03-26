def create_window(arr):
    max_num = 0
    arr.reverse()
    for idx in range(len(arr)):
        max_num = max(arr[idx], max_num)
        arr[idx] = max_num
    return arr


n, A, m = int(input()), list(map(int, input().split())), int(input())
window = []

for idx in range(m - 1, n):
    if not window:
        max_num = 0
        window = create_window(A[idx + 1 - m: idx + 1])
        print(window.pop())
    else:
        max_num = max(A[idx], max_num)
        print(max(max_num, window.pop()))
