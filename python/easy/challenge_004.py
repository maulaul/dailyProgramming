import random, string

PASS_CHOICE = string.ascii_letters + string.digits

def pass_gen(n):
    s = ''
    for i in range(n):
        s += random.choice(PASS_CHOICE)

    return s

def generate_n_pass(n, m):
    pass_list = []
    for i in range(n):
        pass_list.append(pass_gen(m))

    return pass_list

def print_pass(pass_list):
    for p in pass_list:
        print(p)

if __name__ == '__main__':
    print_pass(generate_n_pass(3, 12))
    