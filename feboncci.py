n =100 # required amount of Fibonacci sequence
F = [1, 1]
for x in range(n - 1): # here we have given two numbers
    F.append(F[-2] + F[-1])
print(F)
print(f"F_100 is {F[100]}")
