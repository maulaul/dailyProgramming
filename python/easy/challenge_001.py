def writeToFile(*args):
    #TODO: *save latest userdata from askUser() to a file, for later access.
    with open('challenge_001.txt', 'w') as f:
        data = ",".join(list(args))
        f.write(data)

def askUser():
    name = input("what is your name: ")
    age = input("what is your age: ")
    uname = input("what is your uname: ")

    #print("your name is {name}, you are {age} years old, and your username is {uname}".format(
    #    name=name, age=age, uname=uname
    #))
    #using f-string on Python >= 3.6
    print(f"your name is {name}, you are {age} years old, and your username is {uname}")
    writeToFile(name, age, uname)
    print("saved to file.")

if __name__ == "__main__":
    askUser()
