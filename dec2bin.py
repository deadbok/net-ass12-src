#!/usr/bin/python

import sys, math

def dec2bin(val):
	'''
	Convert from decimal to binary. Output the calculations used along
	the way.

	:param val: Decimal value to convert.
	:return: Binary representation as a string.
	'''
	#Find the highest power of 2 that is lower than the decimal value.
	max_power = 0
	while val >= math.pow(2, max_power + 1):
		max_power += 1
	
	
	#Keep track of the remaining value of the decimal input
	remainder = val
	#Keep track of out current position in the binary output
	current_power = max_power
	#Keep a list of output strings showing the calculations
	calc_vals = list()
	#Loop over the calculations until every binary digit is converted
	#Start from the highest bit
	while current_power > 0:
		#Get the decimal value of the current binary position
		current = math.pow(2, current_power)
		#If this value is lower or equal to the remainder of the decimal
		#number, add a 1 to the binary representation
		if remainder >= current:
			#Save the values for later printing
			calc_vals.append((current_power, (int(math.pow(2, current_power)))))
			#Subtract the current binary value from the decimal remainder
			remainder -= current
		else:
			calc_vals.append((current_power, 0))

		#Go to the next position in the the target binary number
		current_power = current_power - 1

	#Take care of the lowest bit
	if remainder > 0:
		calc_vals.append((0, 1))
	else:
		calc_vals.append((0, 0))


	#Reverse the calculations, seems more intuitive
	calc_vals.reverse()
	#Set up variables for keeping the result
	dec_res = 0
	bin_res = ""
	#Used for formatting the output
	spaces = 0
	#Print the calculations
	for values in calc_vals:
		#Add the current value to the decimal result
		dec_res += values[1]
		#Only print conversion when a bit is set
		if values[1] != 0:
			#The current binary is a one, print the conversion
			print(("0" * (max_power - values[0])) + "1" +
				  ("0" * values[0]) + " = (2^" + str(values[0]) +
				  ") = " + str(values[1]))
			#Add extra spaces
			if len(str(values[0])) > spaces:
				spaces = len(str(values[0]))
			#Add the binary to the result
			bin_res += "1"
		else:
			#Add the binary to the result
			bin_res += "0"

	#Print the result in both binary and decimal
	print(bin_res[::-1] + "	  " + (" " * spaces) + "	" + str(dec_res))
	#Return the binary result
	return(bin_res[::-1])
			
#Run this if called from the command line
if __name__ == "__main__":
	#Get the decimal value from the command lines parameter
	val = int(sys.argv[1])
	#Print what we're doing
	print("Converting decimal: " + sys.argv[1])
	#Convert the value
	dec2bin(val)
