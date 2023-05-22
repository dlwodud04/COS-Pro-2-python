def solution(arr, k):
    list1 = []
    for i in arr:
        for j in i:
            list1.append(j)

    answer = sorted(list1)

    return answer[k-1]