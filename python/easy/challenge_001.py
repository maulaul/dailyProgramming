def writeToFile(name, age, username):
    #TODO: *save latest userdata from askUser() to a file, for later access.
    pass

def askUser():
    name = input("what is your name: ")
    age = input("what is your age: ")
    uname = input("what is your uname: ")

    print("your name is {name}, you are {age} years old, and your username is {uname}".format(
        name=name, age=age, uname=uname
    ))

if __name__ == "__main__":
    askUser()
    