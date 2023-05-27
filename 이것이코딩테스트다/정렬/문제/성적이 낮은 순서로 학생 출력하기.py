N = int(input())


array = []
for _ in range(N):
    # array.append(list(map(int, input().split())))
    input_data = input().split()
    # 튜플은 선언 후 원소가 변하지 않는 경우, 성질이 다른 원소를 가지는 경우 사용
    # 이 경우는 (이름, 성적)으로 서로 다른 성질의 데이터를 튜플로 묶어서 관리. 
    array.append((input_data[0], int(input_data[1])))

array.sort(key=(lambda data: data[1]))

for i in array:
    print(i[0], end=' ')