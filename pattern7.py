# Question 7: Star Pyramid

# Expected output:
        
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

for i in range(1, 6):  # Outer loop controls rows

    for j in range(1, 6-i):  # Prints leading spaces
        print("  ", end="")

    for k in range(1, 2*i):  # Prints odd number of stars
        print("*", end=" ")

    print()  # Moves to next row