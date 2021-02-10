input_score = list(input())
# 누적 프래임 횟수
frame = 1
# 프레임 당 누적 투구 횟수
stack = 0
# 추가 득점 플래그
plus = []
# 결과
answer = 0

def get_score(index):
    # 스트라이크나 스페어로 추가 득점을 하는 경우, 추가 득점을 하는 횟수만큼 리스트에 인덱스 값을 추가
    if input_score[index] == 'S':
        add = 10
        if frame < 10:
            plus.append(index+1)
            plus.append(index+2)
    elif input_score[index] == 'P':
        add = 10 - add_score
        if frame < 10:
            plus.append(index+1)
    elif input_score[index] == '-':
        add = 0
    else:
        add = int(input_score[index])
    return add

for i in range(len(input_score)):
    add_score = get_score(i)
    answer += add_score*(plus.count(i)+1)
    stack += 1
    if (input_score[i] == 'S') | (stack == 2):
        stack = 0
        frame += 1

print(answer)
