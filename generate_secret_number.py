import random

def generate_secret_number():
    """Generates a secret 4-digit number with no repeated digits."""
    digits = list(range(10))
    random.shuffle(digits)
    return "".join(str(d) for d in digits[:4])

#def get_bulls_cows(guess, secret):
#영주 담당

#def play_game():
#이용기 담당
