#################################################
#Tyler Robbins					#
#1/30/14					#
#Integrated DeveLopment Environment for LOLCODE #
#################################################

import platform as plat
import sys
import os

def visible(line):
	try:
		if '"' in line:
			line = line.split('"')[1] #print string
			return line
		
		elif "'" in line:
			line = line.split("'")[1] #works for both forms of quotations
			return line

		elif line in lolvars: #print variable value
			if '"' in lolvars[line]:
				return lolvars[line].strip('"')

			elif "'" in lolvars[line]:
				return lolvars[line].strip("'")

			else:
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

#def restart():
#	if plat.system() == 'Windows':
#		os.system("Interpreter.py")
#	else:
#		os.system("python Interpreter.py")	
#	sys.exit()

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

def argrun(args1, args2):
	if args1 == args2:
		code = lolif["YA RLY"]
		syntaxcheck(code)
	else:
		code = lolif["NO WAI"]
		syntaxcheck(code)

def biggerthan(arg1, arg2):
	if arg1 > arg2:
		return True
	else:
		return False

def lesserthan(arg1, arg2):
	if arg1 < arg2:
		return True
	else:
		return False

def bothsaem(args1, args2):
	linecode = ''	
	code = ''
	line = 0

	while code != 'KTHX':
		code = raw_input("")
		linecode += code + "\n"
	
	linecode = linecode.split("\n")
	linecode.remove('')
#	print linecode
	
	if 'YA RLY' in linecode:
		if args1 in lolvars:
			args1 = lolvars[args1]

		if args2 in lolvars:
			args2 = lolvars[args2]

		if args1 == args2:
#			print "equal"
			line = linecode.index('YA RLY')

			while linecode[line] != 'KTHX':
				line += 1
				if linecode[line] == 'NO WAI':
					line += 2
#					print 'wrong'
				
#				print line
#				print linecode[line]
				syntaxcheck(linecode[line])

		elif args1 != args2:
#			print "not equal"
			line = linecode.index('NO WAI')

			while linecode[line] != 'KTHX':
				line += 1
				if linecode[line] == 'NO WAI':
					line += 1
#					print 'correct'

				syntaxcheck(linecode[line])
	else:
		if "YA RLY" not in linecode:
			print "SyntaxError: Expected 'YA RLY' in <module> at line[1]"
#		else:
#			print "SyntaxError: Expected 'NO WAI' in <module> at line[1]"

def syntaxcheck(code):
	try:
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

		elif " ".join(code.split(" ", 2)[:2]) == 'BOTH SAEM':
			if code == "BOTH SAEM\n":
				print "SyntaxError: Unexpected line break"

			else:
				if "ORLY?" in code:
					arg1 = code.split(" ")[2]
					arg2 = code.split(" ")[4]
					bothsaem(arg1, arg2)
					
				else:
					print "SyntaxError: Invalid Syntax. Expected 'ORLY?'"
	
		elif code.split(" ", 1)[0] == 'BTW':
			pass

		elif code.split(" ", 1)[0] == 'OBTW':
			while code != 'KTHX':
				code = raw_input("")

#		elif code == 'reboot':
#			restart()

		else:
			print "NameError: name '" + code + "' is not defined"

	except Exception as e:
#		print e
		pass

lolkeyword = {'YEP':True, 'NOPE':False}
lolsyntax = ["VISIBLE", "KTHXBYE", "GIMMEH", "BTW", "IZ", "I HAS A"]
#lolerrors = {"IndentationError":"Indentation Error: Expected an indented block.", "SyntaxError": "Syntax Error: Invalid syntax."}
lolvars = {}

print "LOLCODE IDLE 1.0 on " + str(plat.system())
#print 'Type "copyright", "credits", or "license()" for more information'

while True:
	while True:
		code = raw_input(">>> ")

		if code != "\n":
			break

#	print " ".join(code.split(" ", 2)[:2])
	syntaxcheck(code)

	code = ''

nuclear = u'\u2622'
