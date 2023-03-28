def solution(n):
    t = n **(1/2)
    if t% 1 ==0:
        return (t+1)**2
    else:
        return -1