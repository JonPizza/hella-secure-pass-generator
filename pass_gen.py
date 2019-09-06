from random import SystemRandom
import hashlib

rand_num_gen = SystemRandom()

def password_generator(password_length=30):
    '''
    password length max is 64
    '''
    assert password_length <= 64
    while True:
        rand_chars = input('Input some (30-40) random characters: ')
        rand_nums = ''.join([str(rand_num_gen.randrange(100)) for i in range(500)])
        yield hashlib.sha256(f'{rand_chars}{rand_nums}'.encode('utf-8')).hexdigest()[:password_length-1]

password = password_generator()

for i in range(20):
    print(next(password))
