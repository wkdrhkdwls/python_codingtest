def solution(n):
    sum=0
    n = list(map(int, str(n)))
    for i in range(len(n)):
        sum +=n[i]
    return sum
        
        
        