from currency_converter import CurrencyConverter as CC
c=CC()
print("*********************************************")
print("*          THE CURRENCY CONVERTER           *")
print("*********************************************\n\n")

choice=1
while(choice!=3):
    print("1. Want to know the all the Currencies available?\n2. Convert a Currency.\n3. Exit.\n")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        print("The currency list is:")
        for i in c.currencies:
            print(i,end=" , ")
        print("\n")
        continue
    elif(choice==2):
        c1=input("Type your currency\n")
        c1=c1.upper()
        c2=input("Type the currency you want to convert\n")
        c2=c2.upper()
        v=float(input("Enter the value of currency\n"))
        r=c.convert(v,c1,c2)
        print(r)
        print("\n")
        continue
    elif(choice==3):
        print("Thank you to use this currency converter\n")
        break
    else:
        print("Wrong chice\n")
        continue
