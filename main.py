a=int(input("Enter the first number:\n"))
op=input("Enter the operation you want to perform(+,-,*,/):\n")
b=int(input("Enter the second number:\n"))

if op=="+":
    print(f"{a} + {b} = {a+b}")

elif op == "-":
    print(f"{a} - {b} = {a-b}")

elif op =="*":
    print(f"{a}*{b} = {a*b}")

elif op =="/":
    print(f"{a}/{b} = {a/b}")

else:
    print(f"The operation '{op}' is not vaild. ")