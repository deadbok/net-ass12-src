#!/usr/bin/python

import sys, math

#Use the dec2bin function
from dec2bin import dec2bin

if __name__ == "__main__":
    #Split the IP address by the dots
	quad = sys.argv[1].split('.')
    #Print what we're doing
	print("Convertin IPv4 address: " + sys.argv[1])

    #Create a list for the binary value of the ip quads
	bin_res = list()
    #Convert each quad in the IP to binary
	for val in quad:
		print("\nConverting decimal: " + val)
		bin_res.append(dec2bin(int(val)))

    #Print the result
	print("\n" + sys.argv[1] + " = " + bin_res[0] + "." + bin_res[1] + "." +
		  bin_res[2] + "." + bin_res[3])
