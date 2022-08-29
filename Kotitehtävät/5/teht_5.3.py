num = int(input("Syötä numero: "))

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print(f"{num} ei ole alkuluku.")

    else:
        print(f"{num} on alkuluku.")

else:
    print(f"{num} ei ole alkuluku.")
