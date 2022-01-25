import math

def sumavg(n):
    sum=0
    i=1
    while(i<n):
        sum=sum+i
    print("Sum=", sum)
    avg=sum/n
    print("Average =", avg)
n=int(input("Enter n="))
sumavg(n)
