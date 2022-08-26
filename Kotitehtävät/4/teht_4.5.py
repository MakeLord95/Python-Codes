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
            print("Pääsy evätty")
            trys = trys - 1
            input_name = input("Tunnus: ")
            input_pass = input("Salasana: ")

    else:
        break
