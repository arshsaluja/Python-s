bill_amt=float(input("Enter the bill amount:"))
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
        d=float(((5*bill_amt)/100))
        s=float(bill_amt-d)
        print(bill_amt,"                5%           ",s)
    elif((bill_amt>=500) and (bill_amt<1000) ):
        d=float(((2*bill_amt)/100))
        s=float(bill_amt-d)
        print(bill_amt,"                2%           ",s)
    elif((bill_amt>0) and (bill_amt<500)):
        d=float(((1*bill_amt)/100))
        s=float(bill_amt-d)
        print(bill_amt,"                1%           ",s)
    else:
        print("You are not provided with any discount")
