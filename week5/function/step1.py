def maxOfThree (sequence): 
    
    sequence.sort()     
    
    print("Largest number: ", sequence[-1]) 
list_numbers = []
for i in range(3):


  num = input("Please provide your number: ")
  print ("The number you provided is ",num)

  list_numbers.append(num) 


maxOfThree(list_numbers)