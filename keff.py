def keff():
    a = int(input("Введитте число a: "))
    n = int(input("Введите число n: "))
    if a/n != 1:
        print("Частно a и n равно:", a/n)
    else:
        print("Числа не частные, сумма равна:", a+n)
