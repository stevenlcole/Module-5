from telnetlib import theNULL

import py


if __name__ == '__main__':

   # Create a list named food with two elements 'rice' and 'beans'.
   food = ['rice', 'beans'] 
    
   #Append the string 'broccoli' to food using .append().
   food.append('broccoli')

   #Add the strings 'bread' and 'pizza' to food using .extend().
   food.extend(['bread', 'pizza'])
   
   #Print the first two items in the food list using print() and slicing notation.
   print(food[0:2])
    
   #Print the last item in food using print() and index notation.
   print(food[-1])

   #Create a list called breakfast from the string "eggs,fruit,orange juice" 
   # using the split() method.
   bfoods = ('eggs,fruit,orange juice')
   print(type(bfoods))
   breakfast = bfoods.split(',')
   print(breakfast)
   #check to see if list
   print(type(breakfast))

   #Verify that breakfast has 3 elements using the len built-in.
   brlen = len(breakfast)
   print(brlen)
    
   #prompts the user for a floating-point value until they enter stop.
   # Store their entries in a list, and then find the average, min, and max of their entries 
   # and print them those values.
   list = []
   while True:
      num = (input("Enter a number value, or enter stop to stop: "))
      if num == ('stop'):
        break
      #ensure values are floats and assign to list
      value = float(num)
      list.append(value) 
avg = sum(list) / len(list)
minv = min(list)
maxv = max(list) 
print(f'The average is: {avg}.')
print(f'The minimum value is {minv}.')
print(f'The maximum value is {maxv}.')