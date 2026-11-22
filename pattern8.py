# Question 8: Inverted Star Pyramid

# Expected output:
        
#  * * * * * * * * *
#    * * * * * * *
#      * * * * *
#        * * *
#          *


for i in range(5, 0, -1):  # Outer loop: rows decrease from 5 to 1

    for j in range(5-i):  # Prints increasing spaces
        print("  ", end="")

    for k in range(2*i-1):  # Prints decreasing odd number of stars
        print("*", end=" ")

    print()  # Moves to the next row