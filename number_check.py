num = input("Enter a number:")
try:
    inum= int(num)
except:
    inum=-1

if inum > 50:
    print("Thank you for the big number!")
elif inum < 0:
    print("Error: Not a number")
else:
    print("Thank you for the number!")
