#TODO read user.txt and pass.txt
#TODO ask user to input username, password
#TODO if user exist and password correct print something like program unlocked
#TODO if user exist and password incorrect ask 2 more time before program off
#TODO if user doesnt exit, ask continously.
def read_db():
    with open('users005.txt') as f:
        users = {}

        for row in list(f):
            user_data = row.split(",")
            users[user_data[0]] = user_data[1]

    with open('passw005.txt') as f:
        passw = {}

        for row in list(f):
            pasw_data = row.split(",")
            passw[pasw_data[0]] = pasw_data[1]

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
