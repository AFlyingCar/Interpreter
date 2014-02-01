#################################################
#Tyler Robbins					#
#1/30/14					#
#Integrated DeveLopment Environment for LOLCODE #
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

		elif condition1 == "BOTH SAEM":
			if arg1 == arg2:
				syntaxcheck(code)

def syntaxcheck(code):
	if " ".join(code.split(" ", 3)[:3]) == "I HAS A":
		try:
			if "ITZ" in code:
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
		i =0

		for item in code.split(" ")[1:]:
			i+=1
		
		
		iz(code.split(" ")[1])

	elif " ".join(code.split(" ", 2))[0] == 'BOTH SAEM':
		if code.split(" ", len(code)-2)[len(code)-1] != "O RLY?":
			print lolerrors["SyntaxError"]
			condition == "OIC"

		arg1 = code.split(" ")[2]
		arg2 = code.split(" ")[4]
		lolif = {}
		x = 0

		while condition != "OIC":
			condition = raw_input("")

			if condition == "YA RLY":
				code = raw_input("")

				if "\t\t" in code:
					lolif.update({"YA RLY":code})

				else:
					print lolerrors["IndentationError"]

			elif condition.split(" ")[0] == "MEBBE":
				code = raw_input("")
				
				if "\t\t" in code:
					condition = "MEBBE" + str(x)
					lolif.update({condition:code})
				else:
					print lolerrors["IndentationError"]

				x = x + 1

			elif condition == "NO WAI" and "NO WAI" not in lolif:
				code = raw_input("")
				
				if "\t\t" in code:
					lolif.update({"NO WAI":code})
				else:
					print lolerrors["IndentationError"]
		
		def argrun(args1, args2):
			if arg1 == arg2:
				code = lolif["YA RLY"]
				syntaxcheck(code)

			else:
				code = lolif["NO WAI"]
				syntaxcheck(code)

		for item in lolif:
			if arg1 in lolvars:
				if arg2 in lolvars:
					argrun(arg1, arg2)
#					if arg1 == arg2:
#						code = lolif["YA RLY"]
#						syntaxcheck(code)

#					else:
#						code = lolif["NO WAI"]
#						syntaxcheck(code)

				else:
					argrun(arg1, arg2)
			else:
				argrun(arg1, arg2)

#					if arg1 == arg2:
#						code = lolif["YA RLY"]
#			syntaxcheck(code)
#		for item in lolif:
#		if arg1 in lolvars:
#			if arg2 in lolvars:
#				if lolvars[arg1] == lolvars[arg2]:
#					syntaxcheck(code)
#			else:
#				if lolvars[arg1] == arg2:
#					syntaxcheck(code)
#		else:
#			if arg1 == arg2:
#				syntaxcheck(code)
	
	elif code.split(" ", 1)[0] == 'BTW':
		pass
	
	elif code.split(" ", 1)[0] == 'OBTW':
		while True:
			code = raw_input("")
			break

	else:
		print "NameError: name '" + code.split(" ", 1)[0] + "' is not defined"

lolkeyword = {'YEP':True, 'NOPE':False}
lolsyntax = ["VISIBLE", "KTHXBYE", "GIMMEH", "BTW", "IZ", "I HAS A"]
lolerrors = {"IndentationError":"Indentation Error: Expected an indented block.", "SyntaxError": "Syntax Error: Invalid syntax."}
lolvars = {}

print "LOLCODE IDLE 1.0 on " + str(plat.system())
print 'Type "copyright", "credits", or "license()" for more information'

while True:
	code = raw_input(">>> ")

	syntaxcheck(code)

	code = ''

nuclear = u'\u2622'
