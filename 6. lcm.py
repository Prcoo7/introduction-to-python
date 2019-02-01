# the lcm can be derived from the equation: lcm * gcf = num1 * num2
# so we need to get gcf of the given 2 numbers and then we can easily calculate the lcm of the numbers

#gcf function strats... using general approach 
def gcf(m,n):
    ls1 = []            # de.ne list 1 as null list for taking factors of num1
    for i in range(m + 1):
        a = i + 1
        if m%a == 0:
            ls1.append(a)
    
    ls2 = []            # de.ne list 1 as null list for taking factors of num2
    for j in range(n + 1):
        a = j + 1
        if n%a == 0:
            ls2.append(a)
    
    ls3 = []            # de.ne list 3 as null list for taking common factors of num1 and num2

    for k in ls2:
        if k in ls1:
            ls3.append(k)

    return ls3[-1]      # the last factor i.e the greatest common factor will be the gcf also known as hcf

#lcm function starts
def lcm(m, n):
    x = gcf(m, n)
    lcm = (m*n)/x
    return lcm


num1 = int(input("Enter an number : "))
num2 = int(input("Enter another number : "))

print("the lcm of the %d and %d is %d" %(num1, num2, lcm(num1, num2)))