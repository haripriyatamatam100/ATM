print("Welcome to ATM")
restart=('y')
chances=3
balance=100
pin=int(input("Enter pin"))
while chances>0:
    if pin==(1234):
        print("U entered the correct pin")
        while restart not in('n','NO','N','no'):
             print("Press 1 for balance:")
             print("Press 2 for Withdrawl:")
             print("press 3 to credit:")
             print("print other to return")
             option=int(input("Enter an option:"))
             if option ==1:
                 print("Your balance is",balance)
                 break
             elif option ==2:
                 print("Enter the amount to withdraw:")
                 withdraw=int(input())
                 if withdraw in range(balance):
                     balance=balance-withdraw
                     print("Your amount is withdrawn:")
                     break
                 else:
                     print("No sufficient balance")
                     break
             elif option==3:
                 print("Enter the amount to credit:")
                 credit=int(input())
                 balance=balance+credit
                 print("Money credited Successfully:")
                 break
             else:
                 print("Thank u for utilising the services:")
                 break

        restart=input("Enter y or yes to continue:")
        chances-=1
    else:
        print("Enter correct pin:")
        pin=int(input())
        chances-=1
if(chances==0):
    print("try after 24 hours:")
