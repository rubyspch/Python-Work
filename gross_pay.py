hours = input("Enter Hours Worked:")
rate = input("Enter Pay Per Hour:")
try:
    fl_hours=float(hours)
    fl_rate=float(rate) #convert the inputs to floats so you can use arithmatic operators
except:
    print("Error, please enter a numeric value")
    quit() # if input is not numeric code will stop here

if fl_hours>40: #half rate overtime pay added for hours above 40 
    overtime= (fl_hours-40) * (fl_rate*0.5)
    pay= float(overtime) + (fl_rate*fl_hours)
else: #or just rate multiplied by hours
    pay= fl_rate*fl_hours

print("Your Pay is", pay) #print answer