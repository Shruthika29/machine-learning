# Intializing the List and variables
studentslist = []
kg= []
J=0
# Taking Number of Students input from user
a = input("enter no.")
# Looping data for multiple records 
for J in range(int(a)):
 # Taking weights from user
 lb = float(input("enter weights"))
 # Appending the weight of each student to the List
 studentslist.append(lb)
 # Converting the weight from lb to Kilograms
 result = lb*0.453592
 # Appending the weight in Kilograms to the New List
 kg.append(result)
# Printing results
print(studentslist)
print(kg)
