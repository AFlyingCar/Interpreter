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

def iz(args1, args2=None, args3=None, condition1=None):
	linecode = ''
	code = ''
	line = 0

	while code != 'KTHX':
		code = raw_input("")
		linecode += code + '\n'

	linecode = linecode.split("\n")
	linecode.remove('')

#	else:
#		if args1 in lolvars:
#			args1 = lolvars[args1]
#		if args2 in lolvars:
#			args2 = lolvars[args2]
#		if args3 in lolvars:
#			args3 = lolvars[args3]

	if 'YA RLY' in linecode:
		line+=1

		if args2 == None and args3 == None:
			if lolkeyword[args1]:
				while linecode[line] != "KTHX":
					if linecode[line] == "NO WAI":
						line += 1

					syntaxcheck(linecode[line])
					line += 1
		else:
			if condition1 == "BIGGER THAN":
				if args3 == None:
					if args1 > args2:
						while linecode[line] != "KTHX":
							if linecode[line] == "NO WAI":
								line += 1
	
							syntaxcheck(linecode[line])
							line +=1

					else:
						line = linecode.index("NO WAI")
						while linecode[line] != "KTHX":
							syntaxcheck(linecode[line])
							line += 1

				else:
					if condition2 == "BIGGER THAN":
						pass
					elif condition2 == "LESSER THAN":
						pass
					else:
						if args1 > args2 and args3:
							while linecode[line] != "KTHX":
								if linecode[line] == "NO WAI":
									line += 1

								syntaxcheck(linecode[line])
								line += 1
						
						else:
							line = linecode.index("NO WAI")
							while linecode[line] != "KTHX":
								syntaxcheck(linecode[line])
								line += 1

			elif condition1 == "LESSER THAN":
				if args3 == None:
					if args1 > args2:
						while linecode[line] != "KTHX":
							if linecode[line] == "NO WAI":
								line += 1
	
							syntaxcheck(linecode[line])
							line +=1

					else:
						line = linecode.index("NO WAI")
						while linecode[line] != "KTHX":
							syntaxcheck(linecode[line])
							line += 1

				else:
					if condition2 == "BIGGER THAN":
						pass
					elif condition2 == "LESSER THAN":
						pass
					else:
						if args1 > args2 and args3:
							while linecode[line] != "KTHX":
								if linecode[line] == "NO WAI":
									line += 1

								syntaxcheck(linecode[line])
								line += 1
						
						else:
							line = linecode.index("NO WAI")
							while linecode[line] != "KTHX":
								syntaxcheck(linecode[line])
								line += 1
	else:
		print "SyntaxError: Expected 'YA RLY'"
#	if arg1 == 'YEP':
#		arg1 = lolkeyword[arg1]
	
#	elif arg1 == 'NOPE':
#		arg1 = lolkeyword[arg1]

#	else:
#		if condition1 == "BIGGER THAN":
#			if arg1 > arg2:
#				syntaxcheck(code)

#		elif condition1 == "LESSER THAN":
#			if arg1 < arg2:
#				syntaxcheck(code)

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

				syntaxcheck(linecode[line])


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
	
	if 'YA RLY' in linecode:
		if args1 in lolvars:
			args1 = lolvars[args1]

		if args2 in lolvars:
			args2 = lolvars[args2]

		if args1 == args2:
			line = linecode.index('YA RLY')

			while linecode[line] != 'KTHX':
				line += 1
				if linecode[line] == 'NO WAI':
					line += 2

				syntaxcheck(linecode[line])

		elif args1 != args2:
			line = linecode.index('NO WAI')

			while linecode[line] != 'KTHX':
				line += 1
				if linecode[line] == 'NO WAI':
					line += 1

				syntaxcheck(linecode[line])
	else:
		if "YA RLY" not in linecode:
			print "SyntaxError: Expected 'YA RLY' in <module> at line[1]"

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

			print "\n" + vis

		elif code.split(" ", 1)[0] == "KTHXBYE":
			choice = raw_input("The program is still running! Do you want to kill it?(y/n) ")
			if choice == "y":
				sys.exit()

		elif code.split(" ", 1)[0] == "KTHXSYS":
			sys.exit()

		elif code.split(" ", 1)[0] == "GIMMEH":
			lolinput = raw_input(">")
			gimmeh(code.split(" ", 1)[1], lolinput)

		elif code.split(" ")[1] == 'IZ':
			if code.split(" ", 1)[0] in lolvars:
				lolvars[code.split(" ")[0]] = code.split(" ")[2]

			else:
				print "NameError: name '" + line + "' is not defined." #raise NameError if variable is not defined

		elif code.split(" ", 1)[0] == 'IZ':
			i =0

			for item in code.split(" ")[1:]:
				if item == "BIGGER":
					condition = item
					code.remove(item)
				elif item == "LESSER":
					condition = item
					code.remove(item)
				elif item == "THAN":
					code.remove(item)
				else:
					if item in lolvars:
						if arg1 == None:
							arg1 = lolvars[item]
						elif arg2 == None:
							arg2 = lolvars[item]
						else:
							pass

					else:
						pass
				
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

		else:
			print "NameError: name '" + code + "' is not defined"

	except Exception as e:
		pass
