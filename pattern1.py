# Question 1: Solid Square


# Expected output:
        
#         * * * *
#         * * * *
#         * * * *
#         * * * *

for i in range(1,5):  # outer loop run four time (i=1 then 2,3,4) 
        for j in range(1,5): # inner loop run four times for each outer loop
                print("*",end=" ") # print every line * star with a space
        print() # print new line after each loop
        