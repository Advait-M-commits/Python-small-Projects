num = int(input("Enter the first value:\n"))
num2 = int(input("Enter second value:\n"))
op = input("Which Operation you wanna perform? '+' '-' '/' '*' ")
if op == '+':
    print("Combind value of num1 and num2 is: ", num + num2)
elif op == '-':
    print("Substracted value of num1 and num2 is: ", num - num2)
elif op == '*':
    print("The multiplied value would be: ", num * num2)
elif op == '/':
    print("The split value would be: ")
else:
    print("Please choose value operations!")