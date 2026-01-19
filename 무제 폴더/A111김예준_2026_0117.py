T = int(input())
for _ in range(T):
    k = int(input())
    passengers = 0
    for _ in range(k):
        passengers = 2 * passengers + 1
    print(passengers)
