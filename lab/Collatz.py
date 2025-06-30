while True:
    userInput = input("Enter a natural number (or type 'exit' or -1 to stop): ")

    #exit conditions
    if userInput.lower() == "exit" or userInput == "-1":
        print("Thank you and Goodbye")
        break
    #try converting input
    if userInput.isdigit():
        c0 = int(userInput)

        if c0 == 0:
            print("Please enter a number greater than 0.")
            continue

        steps = 0

        while c0 != 1:
            if c0 % 2 == 0:
                c0 = c0//2
            else:
                c0 = 3 * c0 +1
                
            print(c0)
            steps +=1
            
        print("steps = ",steps)
    else:
        print("Invalid input. Enter again:")


