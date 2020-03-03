def solution(numbers):
    #우선, 입력으로 들어온 numbers의 숫자들을 모두 str형으로 바꾼다.
    numbers = [str(x) for x in numbers]
    '''
    1. str로 변환된 문자열을 4번 연속한 문자열을 
    2. 4자리만 슬라이싱 한 것을 key로 이용해
    3. 역순으로 정렬한다.
    3-1. 문자열을 역순으로 정렬한다면, 아래와 같이 정렬된다.
    ["6","10","2"] -> ["6","2","10"]
    '''
    numbers.sort(key = lambda x: (x*4)[:4], reverse = True)
    '''
    numbers의 요소들을 하나씩 answer = ''에 join시키는데, 
    만약 numbers[0] == 0이라면?
    사전순으로 가장 뒤에 있는 숫자가 0이라는 뜻인데, 그럼 모든 숫자가 0이라는 뜻이다.
    따라서 그런 경우에는, answer = "0"으로 초기화 해주는 삼항 연산자를 작성한다.
    '''
    answer = ''.join(numbers) if numbers[0] != "0" else "0"
    #그 뒤, answer를 반환.
    return answer
