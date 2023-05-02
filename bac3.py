def play_game():
    """bulls and cows을 플레이 합니다."""
    secret = generate_secret_number()
    print("Bulls and Cows에 오신 것을 환영합니다. 4자리 숫자를 맞춰 보시지요.")
    num_guesses = 10 # 목숨값 10개 추가.
    while num_guesses > 0: # 목숨 수가 0이 되면 게임 오바.
        guess = input("4자리 숫자를 입력하세요.: ")
        num_guesses -= 1 # 한번 입력할 때 1 감소.
        if guess == secret:
            print("축하합니다. 비밀 숫자를 맞췄습니다.")
            break
        else:
            bulls, cows = get_bulls_cows(guess, secret)
            print("Bulls:", bulls, "Cows:", cows, "남은 목숨 수:", num_guesses) # 게임 점수 및 남은 목숨 수.
