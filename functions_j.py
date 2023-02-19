# Functions and stuff

import pickle


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f'{self.get_username()}'

    def set_username(self, x):
        self.username = x

    def set_password(self, x):
        self.password = x

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password


def two_option(x, y):
    while True:
        try:
            x.strip()
            y.strip()
            prompt = int(input(x + ' : 1' + ' | ' + y + ' : 2' + '   |   '))
            if prompt == 1:
                print('\n')
                return True
            elif prompt == 2:
                print('\n')
                return False
            else:
                print('Invalid Input')
                print('\n')
        except ValueError:
            print('Invalid Input')
            print('\n')


def y_or_n(x):
    while True:
        x.strip()
        prompt = int(input(x + ' y/n : '))
        if prompt == 'y':
            print('\n')
            return True
        elif prompt == 'n':
            print('\n')
            return False
        else:
            print('Invalid Input')
            print('\n')


# For Reading and Writing a .pkl file
def load(x):
    x.strip()
    x = x + '.pkl'
    file = open(x, 'rb')
    return pickle.load(file)


def write(x):
    x.strip()
    x = x + '.pkl'
    file = open(x, 'wb')
    pickle.dump(x, file)
    file.close()


# For avoiding errors in loading a .pkl file
def initialize(x):
    try:
        load(x)
    except FileNotFoundError:
        write(x)
    except EOFError:
        write(x)


# A simple sign in and sign out function
def username_taken(x, y):
    for z in y:
        if z.get_username() == x:
            print('Username Taken')
            return False
    return True


def sign_user(user_list):
    while True:
        if two_option('Log in', 'Sign up'):
            x = input('Username: ').strip()
            y = input('Password: ').strip()
            for z in user_list:
                if z.get_username() == x:
                    if z.get_password() == y:
                        return
            print('Invalid Username or Password')
            print('\n')
        else:
            x = input('Username: ').strip()
            if username_taken(x, user_list):
                y = input('Password: ').strip()
                user_list.append(User(x, y))
                print('Success')
            print('\n')


def sign_user_2(i, user_list, username, password):
    if i:
        for z in user_list:
            if z.get_username() == username:
                if z.get_password() == password:
                    print('Log in')
                    return 'Valid'
        print('Invalid Username or Password')
        return 'Invalid'
    elif not i:
        if username_taken(username, user_list):
            if password != '':
                user_list.append(User(username, password))
                print('Sign Up')
                return 'Valid'
            else:
                print('Invalid Username or Password')
        return 'Invalid'


# Takes in a list of string and ask the user an integer for the input
def module_chooser(y):
    while True:
        try:
            prompt = ''
            i = 1
            for z in y:
                prompt += z + ' : ' + str(i)
                if i == len(y):
                    prompt += '   |   '
                    return int(input(prompt))
                i += 1
                prompt += ' | '

        except ValueError:
            print('Invalid Input')
            print('\n')
