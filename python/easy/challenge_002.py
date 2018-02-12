def cal_force(m, a):
    print(m*a)

def help():
    print('''syntax -> 'function'<space>'inputs' separated by spaces
            example to calculate force of mass 100 and acceleration of 5.
            force 100 5''')

def cal():
    fun = ['force', 'help','exit']
    print('''Just to calculate
            syntax -> 'function'<space>'inputs' separated by spaces''')
    user_in = input('>').split(' ')
    #TODO
    #add dictionary function.
    
if __name__ == '__main__':
    cal()
    