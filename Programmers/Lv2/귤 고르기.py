def solution(k, tangerine):
    dicts = {}
    tangerine.sort()

    for i in tangerine:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1

    dicts = dict(sorted(dicts.items(), key=lambda x: x[1], reverse=True))

    cnt = 0

    for i in dicts:
        if k <= 0:
            return cnt
        k -= dicts[i]
        cnt += 1

    return cnt




