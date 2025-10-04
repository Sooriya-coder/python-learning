#creating a string and storing in an variable
st="string basic operations"
#finding the length of the string using len() function
print(len(st))
#performing slicing operation
#slicing only the word string from the string
print(st[0:6])
#slicing only the word basic from the string
print(st[7:12])
#slicing only the word operations from the string
print(st[13:23])
#slicing all the elements in the string 
print(st[0:])
#slicing the only the first word in the string
print(st[:6])
#slicing all the elements with the step of 2
print(st[0::2])
#assigning a new variable and concatenate the previous string with a new string
op=st+" in python"
#changing the concatenated string into upper case using upper() function
print(op.upper())
