def cal_force(*args):
    values = []
    #print(args)
    for item in args[0]:
        values.append(float(item))
    
    #print(values)
    print(values[0] * values[1])

def fun_help():
    print('''syntax -> 'function'<space>'inputs' separated by spaces
            force --> 'force mass_value acceleration_value' ''')

def cal():
    func_dict = {
                    'force':cal_force
    }

    print('''Just to calculate.\nsyntax -> 'function'<space>'inputs' separated by spaces\ntype 'help' for info. type 'exit' to close program.''', end='\n')
    
    while True:
        user_in = input('> ').split(' ')
        if user_in[0] == 'exit':
            break
        if user_in[0] == 'help':
            fun_help()
        elif (user_in[0] in func_dict.keys()):
            func_dict[user_in[0]](user_in[1:])
        else:
            print("function not available. type 'help' for more info.")

if __name__ == '__main__':
    cal()
