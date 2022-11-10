#User function Template for python3

class Solution:
    def jumpingNums(self, X):
        self.X = X
        mark = 0
        for num in reversed (range (self.X+1)): #reversed range for loop 
            
            #converting num to string and 
            #then appending digits in string 
            
            num_array = [int(digit) for digit in str(num)]
            for i in range (len(num_array)-1):  # if it's 3 digit number then range will be 2
                                                # so we won't be out list index range 
                if abs (num_array[i+1] - num_array[i]) == 1 : # if its like (8-9) or (8-9)
                    mark += 1               # mark this 
                    if mark == len(num_array)-1:
                        return num

                else :
                    mark = 0
                    break 
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.jumpingNums(X))
# } Driver Code Ends
