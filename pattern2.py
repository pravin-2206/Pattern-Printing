# Question 2: Right-Angled Triangle

# Expected output:
        
#         *
#         * *
#         * * *
#         * * * *
#         * * * * *

for i in range(1,6): # Outer loop controls the rows (1 to 5)
        for j in range(1,i+1): # Inner loop controls the columns
                print("*",end=" ")   # Prints stars on the same line
        print()  # print new line after each loop 