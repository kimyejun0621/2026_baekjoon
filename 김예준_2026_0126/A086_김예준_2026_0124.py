# 숫자 -> 영어 단어 매핑
num_to_word = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}

# 입력
M, N = map(int, input().split())

# 숫자들을 영어식으로 변환하고 튜플로 저장
converted = []
for i in range(M, N + 1):
    word = ' '.join(num_to_word[d] for d in str(i))
    converted.append((word, i))

# 영어 기준 정렬
converted.sort()

# 출력: 한 줄에 10개씩
for idx, (_, number) in enumerate(converted):
    print(number, end=' ')
    if (idx + 1) % 10 == 0:
        print()
