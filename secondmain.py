answer=input("Addition or subtraction?").strip().lower()
if answer == "addition":
    x=int(input("pick your first number"))
    y=int(input("pick your second number"))
    print("your answer is: ", x + y)

elif answer == "subtraction":
    a = int(input("pick your first number"))
    z = int(input("pick your second number"))
    print("your answer is: ", a - z)