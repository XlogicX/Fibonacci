#/usr/bin/python

import re
import math
import time
import sys

def errchk(hwmny,int1,int2,int3,int4,errcnt):
	#Sanity check; first 12 numbers don't have 6's
	expression = re.compile(r"^[^6]{1,3}", re.I | re.S)	#expression for no sixes
	if expression.match(str(int3)):		# if it doesn't match
		return							# return
	else:							#otherwise
		if (hwmny > 12):		    # as long as it's less than 12
			return					# no errors
		zints.err()					#but ifnot, errors
	return None

def nofloats():
	return math.floor(zints.int3)

class zeroints:
	int3=int4 = 0	#int3 and int4 are 0
	errcnt = 0		#count the number of errors
	def err(self):
		print "Errors"
		return

hwmny =15			#hwmny variable is 10
int1 =int2 =1		#int1 and int2 are 1
zints = zeroints()	#ints init'd to 0
print "0\n1\n1"

def loop(hwmny,int1,int2,int3,int4,errcnt):
	#Fuck with ()'s below
	while((zints.int4<hwmny)or not(zints.int4>0)and not(zints.int4==0)):	#while int4 is less than hwmny and error checking
		zints.int3 =int1+ int2			#int3 is int1 plus int2
		int1 =int2						#int1 is int2
		string = 'The Values Are'		#string is set to 'The Values Are'
		int2= zints.int3				#int2 is int3
		errchk(hwmny,int1,int2,zints.int3,zints.int4,zints.errcnt)
		print zints.int3				#print int3
		zints.int4= zints.int4+1		#int4 is int4 plus 1
		loop(hwmny,int1,int2,zints.int3,zints.int4,zints.errcnt)		
		continue

loop(hwmny,int1,int2,zints.int3,zints.int4,zints.errcnt)
