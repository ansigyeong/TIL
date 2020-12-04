import datetime


def solution(lines):
    combined_logs = []
    for log in lines:
        logs = log.split(' ')

        # datetime  문자열 형태의 로그를 타임스탬프로 변환함
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f")