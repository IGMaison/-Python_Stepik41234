def chandge(i):
    j = compare(i)
    if i != j:
        A[i], A[j] = A[j], A[i]
        Changes.append((i, j))
        chandge(j)


def compare(i):
    if i * 2 + 2 < n:
        j = i * 2 + 1 if A[i * 2 + 1] < A[i * 2 + 2] else i * 2 + 2
        return j if A[j] < A[i] and j < n else i
    else:
        return i * 2 + 1 if i * 2 + 1 < n and A[i * 2 + 1] < A[i] else i


n, A = int(input()), list(map(int, input().split()))
Changes = []
k = (n - 2) // 2
while k >= 0:
    chandge(k)
    k -= 1
print(len(Changes))
for _ in Changes:
    print(*_)
