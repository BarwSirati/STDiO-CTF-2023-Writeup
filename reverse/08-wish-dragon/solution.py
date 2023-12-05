import random
seed = 1701741064
secret_word = ''

def generate_secret_word():
    global secret_word, secret_word
    random.seed(seed)
    secret_word = ''
    for _ in range(6):
        secret_word += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return secret_word

print(generate_secret_word())