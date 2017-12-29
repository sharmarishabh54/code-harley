print('welcome in harley state bank')

chance=3
balance=5000
# i'm printing some choices here
print('press 1 to check your balance')
print('press 2 to withdraw money')
print('press 3 to return card ')
print('press 4 to add money')
pin=1234
# pin can be change but for now i am setting it as @1234
while(chance>0):
    a=int(input('enter your 4-digit pin__ '))
    if(pin==a):
        print('you entered a correct pin')
        choice=int(input('please enter your choice__ '))
        if(choice==1):
            print('your current balance is ',balance)
            break
        elif(choice==2):
            c=float(input('enter amount__₹ '))
            if(c>balance):
                print('insufficient amount')
                break
            else:
                bal=balance-c
                print('current balance is__',bal)
                print('processing...........')
                print('transaction is being processed')
                print('please collect your cash')
                break
        elif(choice==3):
            print('please wait')
            break
        elif(choice==4):
            print('your current balance is__₹',balance)
            d=float(input('enter a amount you for recharge your wallet__₹.'))
            balance=balance+d
            print('please wait........')
            print('amount has been successfully added to your account')
            print('your current amount is__₹',balance)
            break
    else:
        print('you entered an incorrect pin please try again')
    chance=chance-1
    if(chance==1):
        print('you have entered incorrect pin twice please enter a correct pin to avoid card blockage')
    elif(chance==0):
        print('no more try your card has been temporarily blocked')
print('THANK YOU FOR YOUR KIND VISIT IN "HARLEY STATE BANK"')




