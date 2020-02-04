io=10
c_id=input("Enter your customer id")

if(type(c_id)!=type(io)):
    print("Your customer id cannot be in decimal value")
elif(c_id<0):
    print("Your customer id cannot be less than zero")
elif((c_id>=101) and (c_id<=1000)):
    print("Thanks!!")
    print("Your customer id id is valid")
    bill_amt=int(input("Now please enter the bill amount for discount:"))
    if(bill_amt<0):
        print("Invalid Amount cannot be negative")
        print("Please enter valid amount:")
    else:
        print("DEAR CUSTOMER YOU HAVE A DISCOUNT SCHEME AS FOLLOWS:")
        print("Bill Amount  -     Discount-    ")
        print(">=1000       -        5%   -    ")
        print(">=500 &&<1000-        2%   -    ")
        print(">0 && <500   -        5%   -    ")
        print("Bill Amount-     Discount-     Final Discounted Price-")
        if(bill_amt>=1000):
            d=int(((5*bill_amt)/100))
            s=int(bill_amt-d)
            print(bill_amt,"                5%           ",s)
        elif((bill_amt>=500) and (bill_amt<1000) ):
            d=int(((2*bill_amt)/100))
            s=int(bill_amt-d)
            print(bill_amt,"                2%           ",s)
        elif((bill_amt>0) and (bill_amt<500)):
            d=int(((1*bill_amt)/100))
            s=int(bill_amt-d)
            print(bill_amt,"                1%           ",s)
        else:
            print("You are not provided with any discount")
else:
    print("invalid")
