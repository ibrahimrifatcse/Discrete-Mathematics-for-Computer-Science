#a two-digit number that becomes 7 times smaller after the first digit is deleted
for i in range( 1,100):
    x = i%10
    if(x*7==i):
        print(i," ",x)
 # a number that becomes 57 times smaller       
for i in range(1000,10000):
    n=i%1000
    if(n*57==i):
        print(i," ",n)
        
        
