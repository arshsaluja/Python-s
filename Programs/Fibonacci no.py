"""
fibonacii no
"""

n=int(input("enter the len"))
my_fib=[0,1]        
sum=0
if(n>2):
    for i in range(2,n):
        sum=my_fib[i-1]+my_fib[i-2]
        my_fib.append(sum)
print(my_fib)
    
