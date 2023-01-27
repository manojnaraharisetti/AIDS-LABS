number = int(input("Enter range to terms: "))

a = 0
b = 1
sum_fib = 0
print(a,b, end=" ")
while True:
    sum_fib = a + b
    a = b
    b = sum_fib
    if sum_fib < number:
        print(sum_fib, end=" ")
    else:
        break
