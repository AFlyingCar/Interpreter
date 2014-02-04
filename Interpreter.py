#################################################
#Tyler Robbins					#
#1/30/14					#
#Integrated DeveLopment Environment for LOLCODE #
#################################################

import platform as plat
import sys
import os

lolkeyword = {'YEP':True, 'NOPE':False}
lolsyntax = ["VISIBLE", "KTHXBYE", "GIMMEH", "BTW", "IZ", "I HAS A"]
lolvars = {}

print "LOLCODE IDLE 1.0 on " + str(plat.system())

while True:
	while True:
		code = raw_input(">>> ")

		if code != "\n":
			break

	syntaxcheck(code)

	code = ''

nuclear = u'\u2622'
