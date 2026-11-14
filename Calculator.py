inputone=float(input("Enter first number: "))
inputtwo=float(input("Enter second number: "))



# if inputthree == "+":
#   answer = inputone + inputtwo
#    print(answer)
# elif inputthree == "-":
#    answer = inputone - inputtwo
#    print(answer)
# elif inputthree == "*":
#    answer = inputone * inputtwo
#    print(answer)
# elif inputthree == "/":
#    answer = inputone / inputtwo
#    print(answer)
# else:
#    print("Invalid input")


# Scenario
Operations = ["+", "-", "*", "/"]

#Logic
inputthree=input("Enter the operation: + - * / ")

for option in Operations:
    if option == inputthree:
        if inputthree == "+":
            answer = inputone + inputtwo
            print(answer)
        elif inputthree == "-":
            answer = inputone - inputtwo
            print(answer)
        elif inputthree == "*":
            answer = inputone * inputtwo
            print(answer)
        elif inputthree == "/":
            answer = inputone / inputtwo
            print(answer)
        else:
            print("Invalid input")
    

