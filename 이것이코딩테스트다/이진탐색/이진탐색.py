# 재귀함수로 구현하기
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
    
#     middle = (start + end) // 2
#     if array[middle] == target:
#         return middle
#     elif array[middle] > target:
#         # 재귀함수에서의 주의점 !!!!!!!!!!!!!!!!!! 중요 * 100만개
#         # 재귀함수를 호출할 때는 앞에 return 꼭꼭꼭*100만 붙여주자
#         # 내가 재귀함수를 끝낼 때 얻은 값(여기서는 target의 인덱스)을 최초로 호출한 애한테 리턴해주려는 거 아니야
#         # 그죠? 그럼 재귀함수를 끝낼때만 return 하면 되는 게 아니야 ~ 걔가 리턴되는 거는 '그'함수를 호출한 곳으로 리턴이 되지
#         # 전체 함수를 최초로 호출한 곳으로 리턴이 되는 게 아니야~ 
#         # 계속 계속 리턴이 되서 결론적으로 최초로 호출한 곳으로 리턴이 되는 것이기 때문에
#         # 재귀함수를 호출할 때는 앞에 return을 붙여서 재귀함수에서 리턴한 값을 연쇄적으로 리턴을 해서 
#         # 결론적으로 최초로 함수를 호출한 곳으로 리턴해줘야 됨
#         return binary_search(array, target, start, middle-1)
#     else:
#         return binary_search(array, target, middle+1, end)


# while문으로 구현하기
def binary_search(array, target, start, end):
    while start <= end:
        middle = (start + end) // 2
        if array[middle] == target:
            return middle
        elif array[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    
    
    return None    

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 17
result = binary_search(array, target, 0, len(array)-1)
print('result >> ', result)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)