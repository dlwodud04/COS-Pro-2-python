def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        map1 = bin(arr1[i] | arr2[i])[2:].zfill(n)
        map2 = map1.replace("1", "#").replace("0", " ")
        answer.append(map2)
    return answer