def MultiSum(num1, num2): #This is a function
    if num1 * num2 <= 1000: #Check if the first and second paramters are less than 1000. 
        return num1 * num2 

    else:                   
        return num1+num2




Water = MultiSum(89,54) #Setting a variable to the functions output (with specific inputs).
print(Water) #Print water :)
