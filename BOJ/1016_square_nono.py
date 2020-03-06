# problem_id : 제곱 ㄴㄴ 수
minimum, Maximum = input().split(" ")
def solution(minimum,Maximum)
    import math
    m = int(minimum)
    M = int(Maximum)
    # m ~ M 의 크기를 가지는 1의 리스트
    numbers = [1 for x in range(M - m + 1)]
    # 2 ** 2부터 M 보다 작은 최대의 제곱수까지의 제곱수를 가지는 리스트
    squares = [x ** 2 for x in range(2, int(M ** 0.5) + 1)]
    for square in squares:
        # m보다 큰 최소의 square 의 배수를 구한 후 index 로 사용함.
        '''
        ex)
        m = 5
        square  = 4 라면
        idx = math.ceil(5/4) ( == 1.25 ) * 4 - 5 = 3
        즉, 5,6,7,8...이므로 8은 3번째 요소이다.
        여기서부터 square 씩 더해가면서 numbers list 의 idx 번째 요소를 0으로 바꾸어준다.
        '''
        idx = (math.ceil(m / square) * square) - m
        while idx <= M - m:
            numbers[idx] = 0
            idx += square
    print(numbers.count(1))
