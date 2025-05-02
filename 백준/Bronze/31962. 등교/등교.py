# 버스의 수 N과 지각하지 않기 위한 시간 X를 입력받아요
N, X = map(int, input().split())

# 가장 늦게 출발할 수 있는 시간을 저장할 변수예요
latest_start = -1

# N개의 버스 정보를 하나씩 확인해요
for _ in range(N):
    S, T = map(int, input().split())  # 버스의 출발까지 남은 시간 S와 이동 시간 T를 입력받아요
    if S + T <= X:  # 이 버스를 타면 지각하지 않아요
        if S > latest_start:  # 지금까지 본 버스 중 가장 늦게 출발하는 버스인가요?
            latest_start = S  # 그렇다면 이 버스를 선택해요

# 결과를 출력해요
print(latest_start)
