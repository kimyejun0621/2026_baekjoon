##1. 정수 K가 주어진다.
k = int(input())
stack = []
##2. k만큼 문자열 실행시키기
for i in range(k):
    num = int(input())
    ##3. 값을 저장한후에 0일경우에는 최근에 쓴 수를 지우고 아닐 경우 해당 수를 씀. 해당수를 저장하려면 리스트가 필요
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
    

print(sum(stack))