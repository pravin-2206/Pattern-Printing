# Question 6: Right-Aligned Triangle

# Expected output:
        
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

for i in range(1, 6):  # Outer loop controls rows

    for j in range(1, 6-i):  # Prints leading spaces
        print("  ", end=" ")

    for k in range(1, i+1):  # Prints stars
        print("*", end=" ")

    print()  # Moves to the next row