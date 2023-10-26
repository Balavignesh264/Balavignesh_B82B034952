 # Recursive method to calculate factorial
def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n - 1)

# Input a number
num = int(input("Enter a number: "))

# Calculate factorial using recursive method
result = fact_rec(num)
print("Factorial of no. {} is {}".format(num,result))