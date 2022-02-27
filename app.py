import random

def generate_pw(pw_length, special_char):
    char = 'abcdefghijklmnopqstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    spl_char = '~!@#$%^&*(()_+-={}|[]\:"\';<>?,./'
    random_pw = ''

    if special_char == True:
        char += spl_char

    while len(random_pw) != pw_length:
        random_pw += ''.join(random.choices(char))

    return random_pw