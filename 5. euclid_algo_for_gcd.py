# gcd finds the common greatest factor of numbers.
# it says that gcd(m, n) assuming m > n 
# if n divides m return n 
# otherwise compute gcd(n, m-n) and return that values


def gcd(m, n):
    if m<n:
        (m,n) = (n, m)
    if (m%n) == 0:
        return n
    else:
        return gcd(n, (m-n))

num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))
print("the gcd of %d and %d is %d" %(num1, num2, gcd(num1, num2)))