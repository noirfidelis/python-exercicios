n = int(input('\033[1;35mFala um número aleatório ai menor:\033[m'))
resultado = n % 2
if resultado == 0:
    print(f'\033[1;37mO número {n} é \033[1;97mPAR!')
else:
    print(f'\033[1;37mO número {n} é \033[1;30mÍMPAR!')