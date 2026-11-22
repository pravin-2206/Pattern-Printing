# Question 5: Repeated Row Number Triangle


# Expected output:
        
#         1
#         2 2
#         3 3 3
#         4 4 4 4
#         5 5 5 5 5

for i in range(1,6): # outer loop start with 1 and end with length-1
        for j in range(1,i+1): # inner loop star with 1 to  i+1
                print(i,end=" ") # print i value 
        print() # inner loop complate then move to next line