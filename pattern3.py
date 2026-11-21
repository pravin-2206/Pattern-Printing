# Question 3: Inverted Right-Angled Triangle


# Expected output:
        
        
#         * * * * *
#         * * * *
#         * * *
#         * *
#         *


for i in range(5,0,-1):  # Outer loop: runs from 5 to 1
        for j in range(1,i+1):  # Inner loop: prints stars
                print("*",end=" ")  # Prints stars on the same line
        print() # Move to next line