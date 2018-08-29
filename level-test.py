from random import randint

# 게임 반복 실행
def game_start():    

    com = com_choice()

    while True:
        user = user_choice()
        result = check(user, com)

        strike = result_strike(result)
        ball = result_ball(result, strike)
        result_total(strike, ball)


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
        if user.isdigit() == False:
            print("문자나 기호가 아닌 숫자를 입력해주세요")
            continue
        elif len(user) != 3:
            print("세자리 수를 입력해주세요")
            continue
        elif user[0] == user[1] or user[0] == user[2] or user[1] == user[2]:
            print("서로 다른 수를 입력해주세요")
            continue
        else:
            break
            
    user = [int(i) for i in user]        
    return user


# 컴퓨터와 유저의 수 확인
def check(user, com):

    strike = 0
    ball = 0
    i = 0

    while i < 3:
        if user[i] == com[i]:
            strike += 1
        elif user[i] in com:
            ball += 1
        i += 1
    
    return strike, ball


# 스트라이크 단독 결과 처리
def result_strike(result):

    strike = result[0]
    ball = result[1]

    if strike == 3:
        print("3스트라이크! ")
        print("3개의 숫자를 모두 맞히셨습니다! 축하합니다.")
        game_start()
    elif strike > 0 and ball == 0:
        print("%d 스트라이크" % strike)
    
    return strike


# 볼 단독 결과 처리
def result_ball(result, strike):

    ball = result[1]

    if ball > 0 and strike == 0:
        print("%d볼" % ball)

    return ball


# 스트라이크, 볼 혼합 결과 처리
def result_total(strike, ball):

    if strike == 0 and ball == 0:
        print("포볼")
    elif strike > 0 and ball > 0:
        print("%d 스트라이크 %d볼" % (strike, ball))


game_start()