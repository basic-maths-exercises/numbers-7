import numpy as np

def romanNumeral( N ) :
   # mynumeral is a string variable that will eventually hold the roman numeral
  mynumeral = ""
  # This bit works out how many Cs we need
  nhund = int( np.floor( N / 100 ) )
  # We now put the appropriate number of Cs in the numeral
  for i in range(nhund) : mynumeral = mynumeral + "C"
  # We now subtract the part of the number that we have dealt with 
  # by including the Cs as we would with the base 
  # conversion functions you have written in previous exercises
  rem = N - nhund*100
  # Now work out how many 10s are left in the numbers we need
  ntens = int( np.floor(rem/10) )
  # Subtract the tens that we will deal with in the next few lines
  rem = rem - ntens*10
  # Add an IC if the remainder (once the hundreds are stracted) 
  # is greater than 90
  if ntens==9 : 
    mynumeral = mynumeral + "IC"
    ntens = ntens - 9
  # Add an L if the remainder (once the hundreds are stracted) 
  # is greater than 50 and less than 90  
  elif ntens>=5 : 
    mynumeral = mynumeral + "L"
    ntens = ntens - 5
  # Add an IL if the remainder (once the hundreds are stracted) 
  # is greater than 40 and less than 50 (notice the subtractions 
  # that are done in the previous if statements)
  if ntens==4 : 
    mynumeral = mynumeral + "IL"
  # Add one X for each of the 10 in the remainder (once the hundreds are subtracted)
  # Notice a maximum of three Xs are added
  else :
    for i in range(ntens) : mynumeral = mynumeral + "X"
  # You need to write code here to deal with including any Vs, IVs and Is.  
  if rem==9 : 
     mynumeral = mynumeral + "IX"
     rem = rem - 9
  elif rem>=5 : 
     mynumeral = mynumeral + "V"
     rem = rem - 5 

  if rem==4 : 
     mynumeral = mynumeral + "IV"
  else :
     for i in range(rem) : mynumeral = mynumeral + "I"  
  return mynumeral
  
# Here is some code to test your function
for i in range(1,40) : 
  print("The number",i,"in roman numerals is", romanNumeral(i) )
    
  
