n = 0
x = 1
n = input("Enter: ")
list=[]

def isprime(n):
    '''check if integer n is a prime'''
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

while True:
    x += 1
    
    if isprime(x) == True and n % x == 0:
        list.append(x)
        n /= x

    if not n > 1:
        break

print str(n)
print list
