#Date : 12.10.2022
# This is an Completely weird technique to vonver Binary Numbers to Decimal

def Binary_to_Decimal(n):
    if n == 0 :       # if n is 0 then print 0, we don't need to go through all the trouble
        print (0)
    elif n == 1 :      # if n is 1 then just print 1, no trouble
        print (1)
    str_n = str(n)     # typecasting int to string
     
    str_list = []      # creating an list to store characters
    for ch in str_n :  # looping through str_n
        str_list.append ( ch ) # and appending them in str_list
    str_list = list(reversed(str_list)) # reversing the list items
    i = 0          # a varibale for assigning power of 2
   
    num_list = []  # new list for appending numbers
    
    for num in str_list : # looping through that reversed list
        num_list.append(int(num) * (2**i)) # typcasting characters to int and then append them to num_list
        i += 1            # and keep them multiplying with 2^i and Incrementing by 1 
    
    Sum = sum(num_list)   # Summation of all numbers in list
    
    print ( Sum)
# Function Ends here 
try :
    n = int (input('Enter Integer Number'))
    Binary_to_Decimal(n)
except Exception as  e:
    print (e)

