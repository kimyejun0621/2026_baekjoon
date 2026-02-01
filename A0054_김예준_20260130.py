def solution(board, moves):
    basket = []
    answer = 0
    
    for move in moves:
        # 1. 크레인이 위치한 열(column) 선택 
        # (moves는 1부터 시작하므로 인덱스는 -1 해줘야 함)
        col = move - 1
        
        # 2. 해당 열에서 가장 위에 있는 인형 찾기
        for row in range(len(board)):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0  # 인형을 집었으므로 빈칸(0)으로 만듦
                
                # 3. 바구니에 넣기 전, 마지막 인형과 같은지 확인
                if basket and basket[-1] == doll:
                    basket.pop()    # 연속된 인형 터뜨리기
                    answer += 2     # 사라진 인형은 2개
                else:
                    basket.append(doll) # 바구니에 추가
                
                # 인형을 하나 집었으므로 다음 move로 넘어감
                break
                
    return answer