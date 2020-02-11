# 3차시

score = [(90, 80), (85, 75), (90, 100)]

for i in range(3):
    a = sum(score[i])
    b = sum(score[i]) / 2
    print('{}번 학생의 총점은 {}점이고, 평균은 {}입니다.'.format(i + 1, a, b))