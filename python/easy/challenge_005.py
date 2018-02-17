#TODO read user.txt and pass.txt DONE
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

def check_user(uname, users):
    if uname in users:
        return users[uname]
    else
        print('user/pass incorrect.')
        return ''

def check_pass(pasw, key,passw):
    if pasw == passw[key]:
        return True
    else:
        print('user/pass incorrect.')
        return False

def aProgram();
    users, passw = read_db()
    tries = 0
    logged_in = False
    print('Basic Login.')

    While (tries < 4 and not logged_in)
        uname = input('username: ')
        userpass = input('password: ')

        key = check_user(uname, users)
        
        if key:
            logged_in = check_pass(userpass, key, passw)
            if not logged_in:
                tries += 1
        else:
            tries += 1

    if logged_in:
        print('You are logged in.')
    else:
        print('Program terminate.')

if __name__ == '__main__':
    aProgram()
