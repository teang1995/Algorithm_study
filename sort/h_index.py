def solution(citations):
    citations.sort()
    citations.reverse()
    i = 0
    while i < len(citations) :
        if citations[i] <= i :
            break
        i += 1
    return i

print(solution([3,0,6,1,5]))
#0 1 3 5 6