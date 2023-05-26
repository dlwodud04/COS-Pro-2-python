def solution(board, moves):
    answer = 0
    temp = []
    
    for i in moves : 
        
        for j in range(len(board[0])):
            if board[j][i-1] == 0:
                pass
            
            else :
                temp.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(temp) >= 2:
            if temp[-1] == temp[-2]:
                temp.pop()
                temp.pop()
                answer += 2
    return answer