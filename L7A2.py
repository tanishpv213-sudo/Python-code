units = int(input("please enter the number of units you have consumed: "))

if(units <50):
    print("Your bill is: ", units* 2.60)
    surcharge = 25
elif (units <=100):
 amount = 130 + 162.50 + 526 + ((units - 200) * 2.60) * 8.45
surcharge = 75
total = amount + surcharge
print("/nElectricity bill = %.2f" % total)
