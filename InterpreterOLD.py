#################################################
#Tyler Robbins									#
#1/30/14										#
#Integrated DeveLopment Environment for LOLCODE	#
#################################################

import platform as plat
import sys

def visible(line):
	try:
		if '"' in line:
			line = line.split('"')[1] #print string
			return line
		
		elif line in lolvars: #print variable value
			return lolvars[line]

		else:
			print "NameError: name '" + line + "' is not defined." #raise NameError if variable is not defined

	except Exception as e:
		print e

def gimmeh(var, val):
	try:
		if var.isdigit():
			print "SyntaxError: can't assign to literal"

		else:
			lolvars.update({var:val})

	except Exception as e:
		print e

def iz(arg1, arg2=None, arg3=None, condition1=None):

	while True:
		code = raw_input("""""")
		syntaxcheck(code)

	if arg1 == 'YEP':
		arg1 = lolkeyword['YEP']
	
	elif arg1 == 'NOPE':
		arg1 = lolkeyword['NOPE']

	else:
		if condition1 == "BIGGER THAN":
			if arg1 > arg2:
				syntaxcheck(code)

		elif condition1 == "LESSER THAN":
			if arg1 < arg2:
				syntaxcheck(code)

		elif condition1 == ""

def syntaxcheck(code):
#	if code.split(" ", 2)[0] == "I HAS A":
	if " ".join(code.split(" ", 3)[:3]) == "I HAS A":
		try:
			if "ITZ" in code:
				print code.split(" ", 5)[5]
				print code.split(" ", 3)[3].split(" ")[0]
				gimmeh(code.split(" ", 3)[3].split(" ")[0], code.split(" ", 5)[5])

			else:
				gimmeh(code.split(" ", 3)[3], None)

		except IndexError:
			gimmeh(code.split(" ", 1)[1], None)

	elif code.split(" ", 1)[0] == "VISIBLE":
		vis = visible(code.split(" ", 1)[1])
		if vis == None:
			vis = ''

		print vis

	elif code.split(" ", 1)[0] == "KTHXBYE":
		choice = raw_input("The program is still running! Do you want to kill it?(y/n) ")
		if choice == "y":
			sys.exit()

	elif code.split(" ", 1)[0] == "KTHXSYS":
		sys.exit()

	elif code.split(" ", 1)[0] == "GIMMEH":
		lolinput = raw_input("")
		gimmeh(code.split(" ", 1)[1], lolinput)

	elif code.split(" ")[1] == 'IZ':
		if code.split(" ", 1)[0] in lolvars:
			lolvars[code.split(" ")[0]] = code.split(" ")[2]

		else:
			print "NameError: name '" + line + "' is not defined." #raise NameError if variable is not defined

	elif code.split(" ", 1)[0] == 'IZ':
		for item in code.split(" ")[1:]:
			try:
				
		iz(code.split(" ")[1])

	elif code.split(" ", 1)[0] == 'BTW':
		pass

	else:
		print "NameError: name '" + code.split(" ", 1)[0] + "' is not defined"

lolkeyword = {'YEP':True, 'NOPE':False}
lolsyntax = ["VISIBLE", "KTHXBYE", "GIMMEH", "BTW", "IZ", "I HAS A"]
lolvars = {}

print "LOLCODE IDLE 1.0 on " + str(plat.system())
print 'Type "copyright", "credits", or "license()" for more information'

while True:
	code = raw_input(">>> ")

	syntaxcheck(code)

	code = ''

nuclear = u'\u2622'