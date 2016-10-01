#!/usr/bin/python

import sys, math

def bin2dec(val):
	'''
	Convert from binary to decimal. Output the calculations used along
	the way.

	:param val: String containing the binary number to concert.
	:return: Decimal representation.
	'''
	#Keep track of out current position in the binary input
	current_bit = 0
	#Keep a list of in between results.
	calc_vals = list()
	#Loop over the calculations until every binary digit is converted
	while current_bit <= (len(val) - 1):
		if val[current_bit] == '1':
			#Get the decimal value of the current binary position
			current = math.pow(2, (len(val) - 1) - current_bit)
			#Save the values for later printing
			calc_vals.append(((len(val) - 1) - current_bit, int(current)))

		#Go to the next position in the binary number
		current_bit += 1

	#Set up variables for keeping the result
	dec_res = 0
	bin_res = ""
	#Used for formatting the output
	spaces = 0
	#Print the calculations
	for values in calc_vals:
		#Add the current value to the decimal result
		dec_res += values[1]
		#The current binary is a one, print the conversion
		print(("0" * (len(val) - 1- values[0])) + "1" +
			  ("0" * values[0]) + " = (2^" + str(values[0]) +
			  ") = " + str(values[1]))
		#Add extra spaces
		if len(str(values[0])) > spaces:
			spaces = len(str(values[0]))

	#Print the result in both binary and decimal
	print(val + "      " + (" " * spaces) + "  = " + str(dec_res))
	#Return the decimal result
	return(dec_res)
			
#Run this if called from the command line
if __name__ == "__main__":
	#Get the binary value from the command lines parameter
	val = str(sys.argv[1])
	#Print what we're doing
	print("Converting binary: " + sys.argv[1])
	#Convert the value
	bin2dec(val)
