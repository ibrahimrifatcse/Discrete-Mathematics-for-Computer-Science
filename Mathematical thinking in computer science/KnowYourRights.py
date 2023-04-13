#a two-digit number that becomes 7 times smaller after the first digit is deleted
#naive way
for i in range( 1,100):
    x = i%10
    if(x*7==i):
        print(i," ",x)
 # a number that becomes 57 times smaller       
for i in range(1000,10000):
    n=i%1000
    if(n*57==i):
        print(i," ",n)

#effecient way 
# for the two-digit number problem
for i in range(10, 100):
    x, y = divmod(i, 10)
    if x*7 == 10*y+x:
        print(i)
        
# for the four-digit number problem
for i in range(1000, 10000):
    x, y = divmod(i, 1000)
    if x*57 == 1000*y+x:
        print(i)
        
