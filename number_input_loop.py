def average_answer(answer, list):
    if answer.lower()=="yes":
        print(sum(list)/ len(list))
    elif answer.lower()=="no":
        print("No worries")
    else:
        print("I don't understand sorry")

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


average_question=input("Do you want to know the mean average?")
average_answer(average_question, total)