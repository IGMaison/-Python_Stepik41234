buff, pack_num = map(int, input().split())
packs = [list(map(int, input().split())) for _ in range(pack_num)]
buf_free_time = [0]
for pack in packs:
    if len(buf_free_time) < buff or pack[0] >= buf_free_time[0]:
        if buf_free_time[-1] <= pack[0]:
            buf_free_time.append(pack[0] + pack[1])
            print(pack[0])
        else:
            print(buf_free_time[-1])
            buf_free_time.append(pack[1] + buf_free_time[-1])
        if pack[0] >= buf_free_time[0]:
            buf_free_time.pop(0)
    else:
        print(-1)
