# Program to write binary search 
#Only for beginners to refer to 

elements =[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
min =0
max = len(elements)-1

while(min <=max):
   guess =(min+max)/2
   searchValue = 67 
   if elements[guess]==searchValue:
     print "Found on index",guess
     break
   
   elif elements[guess]<searchValue:
     min =guess+1
     print min

   elif elements[guess]>searchValue:
     max =guess-1     
     print max