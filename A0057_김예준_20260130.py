def solution(cookie):
    answer = 0
    n = len(cookie)
    
    # 1. m은 첫째 아들의 마지막 바구니 인덱스입니다. (경계선 역할)
    for m in range(n - 1):
        # 2. 첫째는 m부터 왼쪽(l)으로, 둘째는 m+1부터 오른쪽(r)으로 확장
        left_sum = cookie[m]
        right_sum = cookie[m+1]
        
        l, r = m, m + 1
        
        while True:
            # 3. 두 아들의 과자 수가 같으면 최대값 갱신
            if left_sum == right_sum:
                answer = max(answer, left_sum)
            
            # 4. 첫째가 더 적거나 같으면 왼쪽으로 한 칸 더 확장 (더 많은 과자를 위해)
            if left_sum <= right_sum and l > 0:
                l -= 1
                left_sum += cookie[l]
            # 5. 둘째가 더 적으면 오른쪽으로 한 칸 더 확장
            elif left_sum >= right_sum and r < n - 1:
                r += 1
                right_sum += cookie[r]
            # 6. 더 이상 확장할 수 없으면 종료
            else:
                break
                
    return answer