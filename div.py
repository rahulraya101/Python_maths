def countDivisibles(A, B, M):
     
    # Variable to store the counter
    counter = 0;
 
    # Running a loop from A to B
    # and check if a number is
    # divisible by M.
    for i in range(A, B):
        if (i % M == 0):
            counter = counter + 1
 
    return counter
A = 100
B = 1000
M = 14

print (countDivisibles(A,B,M))
