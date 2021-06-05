csv = 'Eric,John,Michael;kjgv,Terry,Graham:TerryG;Brian'
friends_list = []
step1 = csv.split(",") 
friends_list = (step1[0:4])
print("step1 ",step1)  
print("friends_list ",friends_list)
step2 = step1[4]
step3 = step2.split (";")
friends_list .append (step3[1])
print("step3 ",step3)