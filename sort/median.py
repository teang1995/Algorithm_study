test_case = int(input())
members = []
for i in range(test_case):
    age, name = input().split()
    members.append([i, int(age), name])
#key=lambda x: (x[1], x[0])와 같은 코드를 이용하면, 두 개의 key를 이용해 정렬이 가능하다.
members.sort(key=lambda x: (x[1], x[0]))
for i in range(test_case):
    print(members[i][1],members[i][2])
