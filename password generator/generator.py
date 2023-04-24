from passwordmeter import test
from urllib.request import urlopen
from os.path import isfile
from random import choice, randint

# download words.txt if it does not exist
if not isfile('words.txt'):
    print ('Downloading words.txt')
    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    with open('words.txt', 'wb') as f:
        # use binary mode to write contents of URL response to file
        f.write(urlopen(url).read())

# load words from words.txt into list
words = open('words.txt', 'r').read().split('\n')

# define list of special characters
special_chars = ['!', '?']


# define func to create password w/ specified number of words, numbers & special chars
def create_password(num_words=2, num_numbers=4, num_special=1):
    pass_str = ''

    for _ in range(num_words):
        pass_str += choice(words).lower().capitalize()
    for _ in range(num_numbers):
        pass_str += str(randint(0,9))
    for _ in range(num_special):
        pass_str += choice(special_chars)
    return pass_str


# define func to generate password, test the strength & print score
def main():
    pass_str = create_password()
    result = test(pass_str)
    strength = result[0]

    print('\n Password: %s'%pass_str)
    print('Strength: %0.5f'%strength)


if __name__=='__main__':
    main()