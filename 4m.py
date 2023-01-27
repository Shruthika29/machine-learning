age = [22, 19, 24, 25, 26, 24, 25, 24]
print("List of age:",age)
# converting list to set
ageCompare=set(age)
# printing
print("Set of age:",ageCompare)
# length of age
length = len(ageCompare)
# printing length
print(" set length:",length)
length2 = len(age)
print("list length:",length2)
# Comparing list and set by conditions
# if it accepts conditon it goes to "IF CONDITION"
# if it doesnot accepts it goes to "ELSE CONDITION"
if length == length2:
   print("length is equal after changing list to set")
else:
   print("length is not equal after changing list to set")
