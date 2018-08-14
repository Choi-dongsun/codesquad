from random import randint

# 게임 반복 실행
def game_start():    

    com = com_choice()

    while True:
        user = user_choice()
        result = check(user, com)
        if result[0] == 3:
            print_result(result)
            game_start()
        else:
            print_result(result)
        

# 컴퓨터의 세수 뽑기
def com_choice():

    number = []
    i = 0

    while i < 3:
        random_number = randint(1, 9)
        if random_number in number:
            continue
        else:
            number.append(random_number)
            i += 1

    return number


# 유저의 세수 뽑기
def user_choice():

    user = 0

    while True:
        user = input('숫자를 입력해주세요. ex)123 : ')
        if len(user) != 3:
            print("올바른 수를 입력해주세요")
            continue
        elif user[0] == user[1] or user[0] == user[2] or user[1] == user[2]:
            print("서로 다른 수를 입력해주세요")
            continue
        else:
            break

    return user


# 컴퓨터와 유저의 수 확인
def check(user, com):

    strike = 0
    ball = 0
    i = 0

    while i < 3:
        if int(user[i]) == com[i]:
            strike += 1
        elif int(user[i]) in com:
            ball += 1
        i += 1
    
    return strike, ball


# 결과 발표
def print_result(result):

    strike = result[0]
    ball = result[1]

    if strike == 0 and ball == 0:
        print("포볼")
    elif strike == 3:
        print("%d 스트라이크" % strike)
        print("3개의 숫자를 모두 맞히셨습니다! 축하합니다.")
    elif strike > 0 and ball == 0:
        print("%d 스트라이크" % strike)
    elif ball > 0 and strike == 0:
        print("%d볼" % ball)
    else:
        print("%d 스트라이크 %d볼" % (strike, ball))


game_start()