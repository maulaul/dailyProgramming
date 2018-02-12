def cal_force(m, a):
    print(m*a)

def fun_help():
    print('''syntax -> 'function'<space>'inputs' separated by spaces
            example to calculate force of mass 100 and acceleration of 5.
            force 100 5''')

def cal():
    func_dict = {
                    'force':cal_force
                    'help':fun_help
    }
    
    print('''Just to calculate
            syntax -> 'function'<space>'inputs' separated by spaces
            type 'help' for info. type 'exit' to close program. ''')
    
    while True:
        user_in = input('>').split(' ')
        if user_in[0] == 'exit':
            break
    
if __name__ == '__main__':
    cal()
