M, N = map(int, input().split())

num_to_word = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}

# 숫자 -> 영어로 바꾸고, 정렬을 위한 리스트 생성
converted = []
for num in range(M, N + 1):
    word = ' '.join(num_to_word[d] for d in str(num))
    converted.append((word, num))

# 영어 기준으로 정렬
converted.sort()

# 정렬된 숫자만 추출해서 출력 (10개씩)
for i in range(len(converted)):
    print(converted[i][1], end=' ')
    if (i + 1) % 10 == 0:
        print()
