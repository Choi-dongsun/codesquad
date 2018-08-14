from random import randint

# 컴퓨터의 세수 뽑기
number = []
i = 0
while i < 3:
    random_number = randint(1, 9)
    if random_number in number:
        continue
    else:
        number.append(random_number)
        i += 1

# 유저의 세수 뽑기
user = 0
while True:
    user = input('숫자를 입력해주세요. ex)123 : ')

# 요구사항에 있지는 않았지만 서로 다른 수여야 하기에 넣었습니다.
    if len(user) != 3:
        print("올바른 수를 입력해주세요")
        continue
    elif user[0] == user[1] or user[0] == user[2] or user[1] == user[2]:
        print("서로 다른 수를 입력해주세요")
        continue

    strike = 0
    ball = 0
    i = 0

    # if int(user[0]) == number[0]:
    #     strike += 1
    # elif int(user[0]) in number:
    #     ball += 1
    # if int(user[1]) == number[1]:
    #     strike += 1
    # elif int(user[1]) in number:
    #     ball += 1
    # if int(user[2]) == number[2]:
    #     strike += 1
    # elif int(user[2]) in number:
    #     ball += 1

    # 위처럼 작성하면 indent depth를 2를 유지할 수 있으나,
    # 비효율적인 것 같아 아래처럼 depth를 3으로 작성하였습니다.

    while i < 3:
        if int(user[i]) == number[i]:
            strike += 1
        elif int(user[i]) in number:
            ball += 1
        i += 1

    if strike == 0 and ball == 0:
        print("포볼")
    elif strike == 3:
        print("%d 스트라이크" % strike)
        print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")
        break
    elif strike > 0 and ball == 0:
        print("%d 스트라이크" % strike)
    elif ball > 0 and strike == 0:
        print("%d볼" % ball)
    else:
        print("%d 스트라이크 %d볼" % (strike, ball))
