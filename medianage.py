ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Calculating the median between the above list of ages.
medianAge= len(ages)//2
medianResult =(ages[medianAge]+ ages[~medianAge])/2
# displaying the result.
print("The median age of list ages is :" ,medianResult)

