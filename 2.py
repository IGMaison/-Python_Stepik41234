n, tree = int(input()), list(map(int, input().split()))
heights = dict()
if n > 1:
    h = 0
    for node in tree:
        prnt = node
        branch_h = 1
        while prnt > -1:
            if heights.get(tree[prnt]):
                branch_h += heights[tree[prnt]]
                break
            branch_h += 1
            prnt = tree[prnt]
        heights[node] = branch_h
        h = max(h, branch_h)
    print(h)
else:
    print(1)
