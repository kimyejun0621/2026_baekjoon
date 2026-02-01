mport sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dx = x1 - x2
    dy = y1 - y2
    dist_sq = dx * dx + dy * dy
    sum_r = r1 + r2
    diff_r = abs(r1 - r2)
    
    if dist_sq == 0:
        if r1 == r2:
            print(-1)  # 무한대의 위치
        else:
            print(0)   # 동심원이지만 반지름 다름
    else:
        if dist_sq > sum_r ** 2:
            print(0)  # 멀리 떨어져 있음
        elif dist_sq < diff_r ** 2:
            print(0)  # 한 원이 다른 원 안에 있음
        elif dist_sq == sum_r ** 2 or dist_sq == diff_r ** 2:
            print(1)  # 외접 or 내접 
        else:
            print(2)  # 두 점에서 만남
