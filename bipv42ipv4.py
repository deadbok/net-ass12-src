#!/usr/bin/python

import sys, math

#Use the bin2dec function
from bin2dec import bin2dec

if __name__ == "__main__":
    #Split the IP address by the dots
	quad = sys.argv[1].split('.')
    #Print what we're doing
	print("Converting binary IPv4 address: " + sys.argv[1])

    #Create a list for the decimal values of the ip quads
	bin_res = list()
    #Convert each quad in the IP to decimal
	for val in quad:
		print("\nConverting binary: " + val)
		bin_res.append(str(bin2dec(val)))

    #Print the result
	print("\n" + sys.argv[1] + " = " + bin_res[0] + "." + bin_res[1] + "." +
		  bin_res[2] + "." + bin_res[3])
