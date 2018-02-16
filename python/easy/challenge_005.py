#TODO read user.txt and pass.txt
#TODO ask user to input username, password
#TODO if user exist and password correct print something like program unlocked
#TODO if user exist and password incorrect ask 2 more time before program off
#TODO if user doesnt exit, ask continously.
def read_db(filename):
    with open('users.txt') as f:
        users = list(f)

    with open('passw.txt') as f:
        passw = list(f)

    return users, passw

def check_user(username, f):
    pass

def check_pass(username, f):
    pass

def aProgram():
    #create program loop here.
    pass

if __name__ == '__main__':
    aProgram()
