import datetime


def solution(lines):
    # 로그의 시작, 종료 시각 저장
    combined_logs = []
    for log in lines:
        logs = log.split(' ')
        print(logs)
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f") # 시간 -> 문자열: strftime / 문자열 -> 시간: strptime
        print(timestamp) 
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        print(timestamp)
        print('__________')
    return



solution([
'2016-09-15 01:00:04.001 2.0s',
'2016-09-15 01:00:07.000 2s'
])