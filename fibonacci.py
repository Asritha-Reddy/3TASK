#FIBONACCI NUMBERS
term1=0
term2=1
print("Fibonacci series upto 10 terms")
i=1
while i<=10:
    print(term1)
    term3=term1+term2
    term1=term2
    term2=term3
    i += 1
print("\nFibonacci series upto the term required")
term1=0
term2=1
n=int(input("Enter the number of terms:"))
i=1
while i<=n:
    print(term1)
    term3=term1+term2
    term1=term2
    term2=term3
    i += 1
