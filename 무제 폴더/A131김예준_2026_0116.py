import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

# 1. 산술평균 (소수 첫째자리에서 반올림)
mean = round(sum(nums) / N)

# 2. 중앙값
median = nums[N // 2]

# 3. 최빈값 (여러 개일 경우 두 번째로 작은 값)
counter = Counter(nums)
freq = counter.most_common()
max_freq = freq[0][1]
modes = [num for num, count in freq if count == max_freq]
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]

# 4. 범위
range_ = nums[-1] - nums[0]

print(mean)
print(median)
print(mode)
print(range_)
