while True:
    userinput = input("Select output (1/2): ")

    if userinput in ('1', '2'):

        if userinput == '1':
            print(userinput)

        if userinput == '2':
            print(userinput)
    else:
        print("Invalid Input")
        print("Exiting")
        break
