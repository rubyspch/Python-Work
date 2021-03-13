num = 0
total=list()
while True:
    val= input("Enter a number: ")
    if val=='done':
        break
    try:
        fval=float(val)
    except:
        print("Invalid input")
        continue
    num=num+1
    total.append(fval)
print("Your total is: ",sum(total))

