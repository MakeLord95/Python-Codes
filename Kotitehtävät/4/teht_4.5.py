username = "python"
password = "rules"
trys = 4
input_name = input("Tunnus: ")
input_pass = input("Salasana: ")

while True:
    if trys != 0:

        if input_name == username and input_pass == password:
            print("Tervetuloa!")
            break

        else:

            trys = trys - 1
            input_name = input("Tunnus: ")
            input_pass = input("Salasana: ")

    else:
        print("Pääsy evätty")
        break
