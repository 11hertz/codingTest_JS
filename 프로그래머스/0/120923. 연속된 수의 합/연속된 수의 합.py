def solution(num, total):
    answer = []
    
    for x in range(-100, 101):
        totalNum = sum(list(range(x, x + num)))
        if totalNum == total: 
            answer = list(range(x, x + num))
            break
    
    return answer