def MissingNumber(array,n):
        #SOLUTION 1
        #j=0
        #z=0
        #array.sort()
        #while j<n-1:
            #if array[j]!=j+1:
                #return j+1
            #else:
                #j+=1
        #return  n
        
        
        #SOLUTION 2
        #To find the sum of numbers in array and subtract it from
        #sum of first n natural numbers
        #Step 1:To find the sum of the numbers in array
        #Step 2:Sum of first n natural numbers
        #Step 3:Find the number
        sumarr=0
        for z in array:
            sumarr=sumarr+z
        sumofn=(n*(n+1))/2
        missingnumber=sumofn-sumarr
        missingnumber=int(missingnumber)
        return missingnumber
n=int(input("Enter a Natural number"))
array=[]
for i in range(0,n-1):
    element=int(input("Enter the number"))
    array.append(element)
Soln=MissingNumber(array,n)
print("Missing number is:",Soln)
