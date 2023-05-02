def play_game():
    """bulls and cows을 플레이합니다."""
    secret = generate_secret_number)
    print("Bulls and Cows에 오신 것을 환영합니다. 4자리 숫자를 맞춰 보시지요.")
    num_guesses = 0
    while True:
        guess = input("4자리 숫자를 입력하세요.: ")
        num_guesses += 1
        if guess == secret:
            print("축하드립니다. 비밀 숫자를", num_guesses, "번 만에 맞췄습니다!")
            break
        else:
            bulls, cows = get_bulls_cows(guess, secret)
            print("Bulls:", bulls, "Cows:", cows)

play_game()
