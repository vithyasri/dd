def sumOfDigitsFrom1ToN(n) : 
  
    result = 0   # initialize result 
   
    for x in range(1, n+1) : 
        result = result + sumOfDigits(x) 
   
    return result 
  
