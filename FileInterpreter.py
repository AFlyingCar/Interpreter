#######################################################################
#Tyler Robbins														  #
#1/29/14															  #
#This is an interpreter for the esoteric programming language, LOLCODE#
#######################################################################

import os
import platform

lolsyntax = ("HAI", "CAN HAS", "I HAS A", "GIMMEH", "IZ", "BIGGER THAN", "ORLY?", "YARLY", "NOWAI", "BTW", "VISIBLE", "KTHX", "KTHXBYE")
lolerrors = {"Syntax Error":SyntaxError, "IOError":IOError, "KeyboardError":KeyboardInterrupt, "NameError":NameError}
lolvars = {}

if platform.system() == 'Windows': #allows Windows compatability
	slash = "\\"
else: #MacOSX/Linux
	slash = "//"

print ">>> Path to LOLCODE: ", #Get the path to the .lol file
loc = raw_input(str(os.getcwd()) + slash + "")

os.chdir(loc)

print ">>> " + str(os.listdir(os.getcwd()))
script = raw_input(">>> LOLCODE: ")

x = open(script, 'r')
code = x.read()


if "HAI" in code.split("\n")[0] and "KTHXBYE" in code.split("\n")[len(code.split("\n"))-1]: #Check for begining and ending syntax

	for item in code.split("\n"): #remove line breaks
		item = item.split("\t") #remove tabs
		print item

		if item in lolsyntax or lolvars:
			if [' '.join(item.split(" ")[0:3])][0] == "I HAS A":
				tempvar = item.split([' '.join(item.split(" ")[0:3])][0]).split(" ")[1] #gets variable name
				tempcast = item.split(tempvar)[1].split(" ")[2]

				lolvars.update({tempvar:tempcast}) #updates lolvars with new variable names

			elif item[1].split(" ")[0] == "VISIBLE":
				print 'test'
				print item
				print item[1].split(" ")[1].split('"')

			else:
				if item not in lolvars:
					raise lolerrors['NameError']("Name '" + item + "' not defined.")

				else:
					raise lolerrors['SyntaxError']("Invalid Syntax")

		else:
#		print ">>> Syntax Error"
			pass
else:
	if "HAI" not in code.split("\n")[0]:
		print ">>> " + lolerrors[0] + "line 1: Expected 'HAI'"

	elif "KTHXBYE" not in code.split("\n")[len(code.split("\n"))]:
		print ">>> " + lolerrors[0] + "line " + len(code.split("\n")) + ": Expected KTHXBYE"

nuclear = u'\u2622'