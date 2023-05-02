# Calculates the number of bulls and cows for a guess.
def get_bulls_cows(guess, secret): # type(int) : guess, secret
    bulls = sum(guess[i] == secret[i] for i in range(4)) # type(bulls) <class 'int'>
    cows = sum(guess.count(digit) and guess.index(digit) != secret.index(digit) for digit in secret) # type(cows) <class 'int'>   
    return bulls, cows
