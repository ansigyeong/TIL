# 슬라이딩 윈도우로 풀이하되, 좀 더 효율적인 접근 전략이 필요함
# 요청량이 변하는 순간은 각 로그의 시작과 끝뿐임을 알 수 있음
# 각 로그별 2번씩 비교 연산만 수행하는 형태로, 쉽게 풀이할 수 있음
# 슬라이딩 윈도우 또한 시작 시각과 끝 시각에 따라 윈도우 범위가 달라지므로, 투 포인터가 결함된 풀이로 볼 수 있음


import datetime


def solution(lines):
    
    combined_logs = [] # combined_logs라는 리스트 변수에는 모든 요청의 시작과 종료가 튜플 형태로 함께 저장됨
    # 로그의 시작 시각(-> 1), 종료 시각(-> -1) 저장
    for log in lines:
        logs = log.split(' ')
        # print(logs)

        # datetime 문자열 형태의 로그를 타임스탬프로 변환함
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp() 
        # strftime 함수를 사용하여 원하는 날짜/시간 포맷으로 출력
        # print(timestamp)
        combined_logs.append((timestamp, -1))
        combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1))

    # 아직 종료되지 않은 누적 요청수 accumulated와 1초 미만 윈도우 범위 내의 모든 요청 수를 합한 값 중에서 최댓값을 결과로 가짐
    accumulated = 0
    max_requests = 1
    combined_logs.sort(key=lambda x: x[0])
    for i, elem1 in enumerate(combined_logs):
        current = accumulated

        # 1초 미만 윈도우 범위 요청 수 계산
        for elem2 in combined_logs[i:]:
            if elem2[0] - elem1[0] > 0.999:
                break
            if elem2[1] > 0:
                current += elem2[1]
        max_requests = max(max_requests, current)
        accumulated += elem1[1]
    return max_requests