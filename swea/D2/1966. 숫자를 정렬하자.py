T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n_list = list(map(int , input().split()))
    n_list.sort()
    n_list_str = [str(x) for x in n_list]
    print(f"#{tc} {' '.join(n_list_str)}")

