from random import randint 	#Used for maze module

#Initialization
serialDigit = ""
serialVowel = "false"
serialReturn = 0
batteries = 0
batteryReturn = 0
batteryCheck = False # Used so that we know the user has checked, even if batteries = 0
parallelPort = False
portCheck = False
portReturn = 0


#Function definitions
	#Setup Modules	
	
def chooseModule():
	module = raw_input("Which module would you like to complete? : ").lower()
	if module == "help" or module == "list" or module == "modules":
		print "List of modules: \n serial  /  wires  /  symbols  /  password  /  battery"
		print " port  /  complicated wires  /  knobs  /  wire sequences"
		print " simon says  /  button  /  who's on first  /  memory"
		print " morse code  /  maze"
		chooseModule()
	elif module == "wires":
		wiresModule()
	elif module == "button":
		buttonModule()
	elif module == "serial":
		serialModule()
	elif module == "symbols":
		symbolsModule()
	elif module == "who's on first":
		whosOnFirstModule()
	elif module == "memory":
		memoryModule()
	elif module == "morse code":
		morseCodeModule()
	elif module == "maze":
		mazeModule()
	elif module == "password":
		passwordModule()
	elif module == "battery":
		batteryModule()
	elif module == "port":
		portModule()
	elif module == "complicated wires":
		complicatedWiresModule()
	elif module == "wire sequences":
		wireSequencesModule()
	elif module == "simon says":
		simonSaysModule()
	elif module == "knobs":
		knobsModule()
	elif module == "quit":
		exit(0)
	else:
		print "Something was wrong with your input, try again"
		chooseModule()	
		
def batteryModule():
	global batteries
	global batteryCheck
	global batteryReturn
	batteries = raw_input("How many batteries are there? : ")
	batteryCheck = True
#Check if it is a valid number
	if batteries.isdigit() == False:
		print "You did not enter a valid number. Try again."
		batteryModule()
#Convert from string to int
	batteries = int(batteries)
	if batteryReturn == 0:
		chooseModule()
	elif batteryReturn == 1:
		batteriesReturn = 0

def portModule():
#Check if there is a parallel port (for complicated wires)
	global parallelPort
	global portCheck
	global portReturn
	port = raw_input("Is there a parallel port? (y/n): ").lower()
	portCheck = True
	if port != "y" and port != "n":
		print "You gave an incorrect input. Try again."
		portModule()
	if port == "y":
		parallelPort = True
	elif port == "n":
		parallelPort = False
#Decides where to return
	if portReturn == 0:
		chooseModule()
	elif portReturn == 1:
		portReturn = 0
		
def serialModule(): 
#Variables
	global serialDigit, serialVowel, serialReturn
	possibleInputs = ["nn","yn","ny","yy"]
	serialNumber = raw_input("Serial number odd/vowel? (nn/yn/ny/yy) : ")
#Quit case
	if serialNumber == "quit":
		chooseModule()
#Incorrect Case
	if possibleInputs.count(serialNumber) == 0:
		print "Incorrect input, try again."
		serialModule()
#Setting odd or even
	if serialNumber[0] == "n":
		serialDigit = "even"
	else:
		serialDigit = "odd"
#Setting vowel or no vowel
	if serialNumber[1] == "n":
		serialVowel = "false"
	else:
		serialVowel = "true"
#Choosing where to return
	if serialReturn == 0:
		chooseModule()
	elif serialReturn == 1:
		serialReturn = 0;
		
	#Regular Modules
	
def wiresModule():
#Variables
	global serialReturn
	wires = raw_input("Input the sequence of wires: ").lower()
	wiresLength = len(wires)
#Different cases
	if wires == "quit":
		chooseModule()
	elif wiresLength < 3:
		print "Something was wrong with your input, try again"
		wiresModule()
	elif wiresLength == 3:	
		if 'r' not in wires:
			print "Cut the second wire"
		elif wires[wiresLength - 1] == 'w':
			print "Cut the last wire"
		elif wires.count('b') > 1:
			print "Cut the last blue wire"
		else:
			print "Cut the last wire"
	elif wiresLength == 4: 
		if serialDigit == "":
			 serialReturn = 1
			 serialModule();
		if wires.count('r') > 1 and serialDigit == "odd":
			print "Cut the last red wire"
		elif wires[wireLength - 1] == 'y' and 'r' not in wires:
			print "Cut the first wire"
		elif wires.count('b') == 1:
			print "Cut the first wire"
		elif wires.count('y') > 1:
			print "Cut the last wire"
		else:
			print "Cut the second wire"
	elif wiresLength == 5:
		if serialDigit == "":
			 serialReturn = 1
			 serialModule();
		if wires[wireLength - 1] == 'k' and serialDigit == "odd":
			print "Cut the fourth wire"
		elif wires.count('r') == 1 and wires.count('y') > 1:
			print "Cut the first wire"
		elif wires.count('k') == 0:	
			print "Cut the second wire"
		else: 
			print "Cut the first wire"
	elif wiresLength == 6:
		if serialDigit == "":
			 serialReturn = 1
			 serialModule();
		if wires.count('y') == 0 and serialDigit == "odd":
			print "Cut the third wire"
		elif wires.count('y') == 1 and wires.count('w') > 1:
			print "Cut the fourth wire"
		elif wires.count('r') == 0:
		 	print "Cut the last wire"
		else:
		 	print "Cut the fourth wire"
	elif wiresLength > 6:
		print "Something was wrong with your input, try again"
		wiresModule()
#Return to home
	chooseModule()

def complicatedWiresModule():
	global serialReturn, serialVowel, serialDigit
	global batteryReturn, batteryCheck, batteries
	global portReturn, portCheck, parallelPort
#Setting up
	if serialDigit == "":
		serialReturn = 1
		serialModule()
	if batteryCheck == False:
		batteryReturn = 1
		batteryModule()
	if portCheck == False:
		portReturn = 1
		portModule()
#More set up
#C = 1, D = 2, S = 3, P = 4, B = 5
	wiresDict = {"nn": 1, "rnn": 3, "bnn": 3, "rbnn": 3, "ny": 2, "rny": 5, "bny": 4, 
			 "rbny": 3, "yn": 1, "ryn": 1, "byn": 2, "rbyn": 1, "yy": 5, "ryy": 5, 
			 "byy": 4, "rbyy": 2}
	wire = raw_input("Input wire features (red,blue,star,LED) : ")
	if wire == "quit":
		chooseModule()
	elif wiresDict.has_key(wire) == False:
		print "Incorrect input, try again. Examples: rbyn, ny, bny"
		complicatedWiresModule()
#Returning an answer based on the dictionary
	answer = wiresDict[wire]
	if answer == 1: 
		print "Cut the wire"
	elif answer == 2:
		print "Don't cut the wire"
	elif answer == 3:
		if serialDigit == "even":
			print "Cut the wire"
		else:
			print "Don't cut the wire"
	elif answer == 4:
		if parallelPort == True:
			print "Cut the wire"
		else:
			print "Don't cut the wire"
	elif answer == 5:
		if batteries >= 2:
			print "Cut the wire"
		else:
			print "Don't cut the wire"	
	complicatedWiresModule()
	
def wireSequencesModule():
#Setting up the three lists (1 = A, 2 = B, 3 = C, 4 = AB, 5 = AC, 6 = BC, 7 = ABC)
	redList = [3,2,1,5,2,5,7,4,2]
	blueList = [2,5,2,1,2,6,3,5,1]
	blackList = [7,5,2,5,2,6,4,3,3]
	aList = [1,4,5,7]
	bList = [2,4,6,7]
	cList = [3,5,6,7]
	redPointer = 0
	bluePointer = 0
	blackPointer = 0
	possibleWires = ["r","b","k","n"]
	sequence = ""
	while sequence != "quit":
		sequence = raw_input("Enter sequence of 3 wires "
 							 "(red(r)/blue(b)/black(k)/none(n)): ")
 		input = True
 		#Checking the validity of the input
		if len(sequence) != 3:
			input = False
		else:
			for i in xrange(0,3):
				if sequence[i] not in possibleWires:
					input = False
	#Giving an output and moving down the lists
		if input == True:
			if sequence[0] == "r":
				if redList[redPointer] in aList:
					print "Cut  ",
				else:
					print "Don't cut  ",
				redPointer += 1
			elif sequence[0] == "b":
				if blueList[bluePointer] in aList:
					print "Cut  ",
				else:
					print "Don't cut  ",
				bluePointer += 1
			elif sequence[0] == "k":
				if blackList[blackPointer] in aList:
					print "Cut  ",
				else:
					print "Don't cut  ",
				blackPointer += 1
			if sequence[1] == "r":
				if redList[redPointer] in bList:
					print "Cut  ",
				else:
					print "Don't cut  ",
				redPointer += 1
			elif sequence[1] == "b":
				if blueList[bluePointer] in bList:
					print "Cut  ",
				else:
					print "Don't cut  ",
				bluePointer += 1
			elif sequence[1] == "k":
				if blackList[blackPointer] in bList:
					print "Cut  ",
				else:
					print "Don't cut  ",
				blackPointer += 1
			if sequence[2] == "r":
				if redList[redPointer] in cList:
					print "Cut  ",
				else:
					print "Don't cut  ",
				redPointer += 1
			elif sequence[2] == "b":
				if blueList[bluePointer] in cList:
					print "Cut  ",
				else:
					print "Don't cut  ",
				bluePointer += 1
			elif sequence[2] == "k":
				if blackList[blackPointer] in cList:
					print "Cut  ",
				else:
					print "Don't cut  ",
				blackPointer += 1
			print ""
		if input == False and sequence != "quit":
			print "Incorrect input. Try again."			
 	chooseModule()
	
def buttonModule():
	global batteries, batteryReturn, batteryCheck
	check1 = False
	check2 = False
	check3 = False
	check4 = False
	possibleButtons = ["blue","white","yellow","red","b","w","y","r"]
	#Check the number of batteries
	if batteryCheck == False:
		batteryReturn = 1
		batteryModule()
	#Depending on batteries, check different things
	if batteries > 2:
		while check1 == False:
			frk = raw_input("Is there a lit FRK indicator (y/n)? : ").lower()
			if frk == "quit":
				chooseModule()
			if frk == "y" or frk == "n":
				check1 = True
			else:
				print "Incorrect input. Try again."
			if frk == "y":
				print "Press and immediately release the button"
				chooseModule()
	if batteries > 1:
		while check2 == False:
			detonate = raw_input("Does the button say detonate (y/n)? : ").lower()
			if detonate == "quit":
			 	chooseModule()
			if detonate == "y" or detonate == "n":
				check2 = True
			else:
				print "Incorrect input. Try again."
			if detonate == "y":
				print "Press and immediately release the button"
				chooseModule()
	color = ""
	while check3 == False:
		color = raw_input("What color is the button? : ").lower()
		if color == "quit":
			chooseModule()
		if color in possibleButtons:
			check3 = True
		else:
			print "Incorrect input. Try again."
	if color == "red":
		while check4 == False:
			hold = raw_input("Does the button say hold (y/n)? : ").lower()
			if hold == "quit":
				chooseModule()
			elif hold == "y":
				print "Press and immediately release the button"
				chooseModule()
			elif hold == "n":
				check4 = True
			else:
				print "Incorrect input. Try again."
	#All remaining cases			
	print "Hold down button and read the color of the strip:"
	print " Blue strip: release when the countdown timer has a 4 in any position"
	print " White strip: release when the countdown timer has a 1 in any position"
	print " Yellow strip: release when the countdown timer has a 5 in any position"
	print " Any other color strip: release when the countdown timer has a 1 in any",
	print "position"
	print ""
	chooseModule()
			
def symbolsModule():
#List of all of the symbols
 	allSymbols = ["q","pyramid","slide","z","cat","h","boob","6","euro","#","ae","psi",
				  "n","omega","corkscrew","star","?","c","nose","ik","2","p","boot",
				  "smiley","snake"]	
#Possible lists of symbols	
	symbols1 = ["q","pyramid","slide","z","cat","h","boob"]
	symbols2 = ["euro","q","boob","corkscrew","star","h","?"]
	symbols3 = ["c","nose","corkscrew","ik","2","slide","star"]
	symbols4 = ["6","p","boot","cat","ik","?","smiley"]
	symbols5 = ["psi","smiley","boot","boob","p","snake","star"]
	symbols6 = ["6","euro","#","ae","psi","n","omega"]
	symbols = [symbols1,symbols2,symbols3,symbols4,symbols5,symbols6]
#Setup
	sortTemp = 0
	indexTemp = 0 
	symbolsList = []
	indexList = [0,0,0,0]
	sortList = [1,2,3,4]
	symbolsCount = 0
	listFound = "false"
	print "Available symbols:"
	for i in xrange(0,len(allSymbols)):
		print allSymbols[i],
	print ""
#Ask for symbols
	firstSymbol = raw_input("First symbol: ").lower()
	if firstSymbol == "quit":
		chooseModule()
	secondSymbol = raw_input("Second symbol: ").lower()
	if secondSymbol == "quit":
		chooseModule()
	thirdSymbol = raw_input("Third symbol: ").lower()
	if thirdSymbol == "quit":
		chooseModule()
	fourthSymbol = raw_input("Fourth symbol: ").lower()
	if fourthSymbol == "quit":
		chooseModule()
#Loop to find correct list
	for i in xrange(0,len(symbols)):
		symbolsList = symbols[i]
		symbolsCount = 0
		for j in xrange(0,len(symbols1)):
			if firstSymbol == symbols[i][j]:
				symbolsCount += 1
			elif secondSymbol == symbols[i][j]:
				symbolsCount += 1
			elif thirdSymbol == symbols[i][j]:
				symbolsCount += 1
			elif fourthSymbol == symbols[i][j]:
				symbolsCount += 1
		if symbolsCount == 4:
			listFound = "true"
			break
#Case where something was incorrectly entered
	if listFound == "false":
		print "Your entries did not match any of the lists. Try again."
		symbolsModule()
#Finding symbol indices in the list
	for i in xrange(0,len(symbols1)):
		if symbolsList[i] == firstSymbol:
			indexList[0] = i
		elif symbolsList[i] == secondSymbol:
			indexList[1] = i
		elif symbolsList[i] == thirdSymbol:
			indexList[2] = i
		elif symbolsList[i] == fourthSymbol:
			indexList[3] = i
#Swapping to find correct order		
	for i in xrange(0,4):
		for j in xrange(0,3):
			if indexList[j] > indexList[j+1]:
				indexList[j],indexList[j+1] = indexList[j+1],indexList[j] 
				sortList[j],sortList[j+1] = sortList[j+1],sortList[j] 
#Correct order
	print "Correct order:",
	for i in xrange(len(sortList)):
		if sortList[i] == 1:
			print firstSymbol,
		if sortList[i] == 2:
			print secondSymbol,
		if sortList[i] == 3:
			print thirdSymbol,
		if sortList[i] == 4:
			print fourthSymbol,
	print ""		
	chooseModule()

def simonSaysModule():
	global serialDigit, serialReturn, serialVowel
#Setting up color conversions
	noneVowel = {"r" : "blue", "b" : "red", "g" : "yellow", "y" : "green"}
	oneVowel = {"r" : "yellow", "b" : "green", "g" : "blue", "y" : "red"}
	twoVowel = {"r" : "green", "b" : "red", "g" : "yellow", "y" : "blue"}
	noneNoVowel = {"r" : "blue", "b" : "yellow", "g" : "green", "y" : "red"}
	oneNoVowel = {"r" : "red", "b" : "blue", "g" : "yellow", "y" : "green"}
	twoNoVowel = {"r" : "yellow", "b" : "green", "g" : "blue", "y" : "red"}
	possibleColors = ["r","b","g","y"] #Used to check for correct input
	possibleStrikes = ["0","1","2"]
#Checking for serial number
	if serialDigit == "":
		serialReturn = 1
		serialModule()
#Get setup input
	strikes = ""
	pattern = ""
	input = True
	list = {}
	strikes = raw_input("Enter the number of strikes: ")
	if strikes not in possibleStrikes:
		print "Incorrect input. Try again"
		simonSaysModule()
#Set the correct list
	if serialVowel == "true" and strikes == "0":
		list = noneVowel
	elif serialVowel == "true" and strikes == "1":
		list = oneVowel
	elif serialVowel == "true" and strikes == "2":
		list = twoVowel	
	elif serialVowel == "false" and strikes == "0":
		list = noneNoVowel
	elif serialVowel == "false" and strikes == "1":
		list = oneNoVowel	
	elif serialVowel == "false" and strikes == "2":
		list = twoNoVowel	
#Convert color input to output		
	while pattern != "quit":
		pattern = raw_input("Enter the pattern of colors (r/b/g/y): ")
		input = True 
		for i in xrange(len(pattern)):
			if pattern[i] not in possibleColors:
				input = False
		if input == True:
			for i in xrange(len(pattern)):
				print list[pattern[i]],
				print "  ",
			print ""
		elif input == False and pattern != "quit":
			print "Incorrect input. Try again."
	chooseModule()
	
def whosOnFirstModule():
#1	4
#2	5
#3	6 
	step1 = {"yes": 2, "first": 4, "display": 6, "okay": 4, "says": 6, "nothing" : 2, "":
			 3, "blank": 5, "no": 6, "led": 2, "lead": 6, "read": 5, "red": 5, "reed": 3,
			 "leed": 3, "hold on": 6, "you": 5, "you are": 6, "your": 5, "you're": 5, 
			 "ur": 1, "there" : 6, "they're:": 3, "their": 5, "they are": 2, "see": 6, 
			 "c": 4}
#Indexes in above dict used in combination w/ translations below
	step1Translations = ["nothing","top left","middle left","bottom left","top right",
						 "middle right","bottom right"]
	step2 = {"ready": "YES, OKAY, WHAT, MIDDLE, LEFT, PRESS, RIGHT, BLANK, READY, NO, " 
		     		"FIRST, UHHH, NOTHING, WAIT",
		     "first": "LEFT, OKAY, YES, MIDDLE, NO, RIGHT, NOTHING, UHHH, WAIT, READY, " 
		     		"BLANK, WHAT, PRESS, FIRST",
		     "no": "BLANK, UHHH, WAIT, FIRST, WHAT, READY, RIGHT, YES, NOTHING, LEFT, " 
		     		"PRESS, OKAY, NO, MIDDLE",		     
		     "blank": "WAIT, RIGHT, OKAY, MIDDLE, BLANK, PRESS, READY, NOTHING, NO, "
		     		"WHAT, LEFT, UHHH, YES, FIRST",
		     "nothing": "UHHH, RIGHT, OKAY, MIDDLE, YES, BLANK, NO, PRESS, LEFT, WHAT, "
		     		"WAIT, FIRST, NOTHING, READY",
		     "yes": "OKAY, RIGHT, UHHH, MIDDLE, FIRST, WHAT, PRESS, READY, NOTHING, YES, "
		     		"LEFT, BLANK, NO, WAIT",
		     "what": "UHHH, WHAT, LEFT, NOTHING, READY, BLANK, MIDDLE, NO, OKAY, FIRST, "
		     		"WAIT, YES, PRESS, RIGHT",
			 "uhhh": "READY, NOTHING, LEFT, WHAT, OKAY, YES, RIGHT, NO, PRESS, BLANK, "
			 		"UHHH, MIDDLE, WAIT, FIRST", 
			 "left": "RIGHT, LEFT, FIRST, NO, MIDDLE, YES, BLANK, WHAT, UHHH, WAIT, "
			 		"PRESS, READY, OKAY, NOTHING",
			 "right": "YES, NOTHING, READY, PRESS, NO, WAIT, WHAT, RIGHT, MIDDLE, LEFT, "
			 		"UHHH, BLANK, OKAY, FIRST",
			 "middle": "BLANK, READY, OKAY, WHAT, NOTHING, PRESS, NO, WAIT, LEFT, "
			 		"MIDDLE, RIGHT, FIRST, UHHH, YES",
			 "okay": "MIDDLE, NO, FIRST, YES, UHHH, NOTHING, WAIT, OKAY, LEFT, READY, "
			 		"BLANK, PRESS, WHAT, RIGHT",
			 "wait": "UHHH, NO, BLANK, OKAY, YES, LEFT, FIRST, PRESS, WHAT, WAIT, "
			 		"NOTHING, READY, RIGHT, MIDDLE",
			 "press": "RIGHT, MIDDLE, YES, READY, PRESS, OKAY, NOTHING, UHHH, BLANK, "
			 		"LEFT, FIRST, WHAT, NO, WAIT",
			 "you": "SURE, YOU ARE, YOUR, YOU'RE, NEXT, UH HUH, UR, HOLD, WHAT?, YOU, "
			 		"UH UH, LIKE, DONE, U",
			 "you are": "YOUR, NEXT, LIKE, UH HUH, WHAT?, DONE, UH UH, HOLD, YOU, U, "
			 		"YOU'RE, SURE, UR, YOU ARE",
			 "your": "UH UH, YOU ARE, UH HUH, YOUR, NEXT, UR, SURE, U, YOU'RE, YOU, "
			 		"WHAT?, HOLD, LIKE, DONE",
			 "you're": "YOU, YOU'RE, UR, NEXT, UH UH, YOU ARE, U, YOUR, WHAT?, UH HUH, "
			 		"SURE, DONE, LIKE, HOLD",
			 "ur": "DONE, U, UR, UH HUH, WHAT?, SURE, YOUR, HOLD, YOU'RE, LIKE, NEXT, "
			 		"UH UH, YOU ARE, YOU",
			 "u": "UH HUH, SURE, NEXT, WHAT?, YOU'RE, UR, UH UH, DONE, U, YOU, LIKE, "
			 		"HOLD, YOU ARE, YOUR",
			 "uh huh": "UH HUH, YOUR, YOU ARE, YOU, DONE, HOLD, UH UH, NEXT, SURE, "
			 		"LIKE, YOU'RE, UR, U, WHAT?",
			 "uh uh": "UR, U, YOU ARE, YOU'RE, NEXT, UH UH, DONE, YOU, UH HUH, LIKE, "
			 		"YOUR, SURE, HOLD, WHAT?",
			 "what?": "YOU, HOLD, YOU'RE, YOUR, U, DONE, UH UH, LIKE, YOU ARE, UH HUH, "
			 		"UR, NEXT, WHAT?, SURE",
			 "done": "SURE, UH HUH, NEXT, WHAT?, YOUR, UR, YOU'RE, HOLD, LIKE, YOU, U, "
			 		"YOU ARE, UH UH, DONE",
			 "next": "WHAT?, UH HUH, UH UH, YOUR, HOLD, SURE, NEXT, LIKE, DONE, YOU ARE, "
			 		"UR, YOU'RE, U, YOU",
			 "hold": "YOU ARE, U, DONE, UH UH, YOU, UR, SURE, WHAT?, YOU'RE, NEXT, HOLD, "
			 		"UH HUH, YOUR, LIKE",
			 "sure": "YOU ARE, DONE, LIKE, YOU'RE, YOU, HOLD, UH HUH, UR, SURE, U, "
			 		"WHAT?, NEXT, YOUR, UH UH",
			 "like": "YOU'RE, NEXT, U, UR, HOLD, DONE, UH UH, WHAT?, UH HUH, YOU, LIKE, "
			 		"SURE, YOU ARE, YOUR"
		     }
	displayLabel = ""
	step2check = False
	displayLabel = raw_input("What is the label on the display? : ").lower()
	#Quit and incorrect cases
	if displayLabel == "quit":
		chooseModule()
	if step1.has_key(displayLabel) == False:
		print "Incorrect input. Try again."
		whosOnFirstModule()
	#If makes it past above tests, continues on
	buttonNumber = step1[displayLabel]
	buttonLocation = step1Translations[buttonNumber]
	print ""
	print "Press", buttonLocation, "button"
	print ""
	while step2check == False:
		step2check = True
		buttonLabel = raw_input("What is the label on the button? : ").lower()
		if buttonLabel == "quit":
			chooseModule()
		if step2.has_key(buttonLabel) == False:
			print "Incorrect input. Try again."
			step2check = False
		else:
			print ""
			print step2[buttonLabel]
			print ""
	whosOnFirstModule()

def morseCodeModule():
	#Set up lists
	morseTranslations = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e",
						 "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j",
						 "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o",
						 ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
						 "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y",
						 "--..": "z"}
	morseWords = ["shell", "halls", "slick", "trick", "boxes", "leaks", "strobe",
				  "bistro", "flick", "bombs", "break", "brick", "steak", "sting",
				  "vector", "beats"]
	morseFreqs = [3.505, 3.515, 3.522, 3.532, 3.535, 3.542, 3.545, 3.552, 3.555, 3.565,
				 3.572, 3.575, 3.582, 3.592, 3.595, 3.600]
	letters = []
	wordsLeft = []
	for i in xrange(len(morseWords)):
		wordsLeft.append(0)
	morseCheck = False
	count = 1
	while morseCheck == False:
		morseCode = raw_input("Enter code for one letter : ")
		if morseCode == "quit":
			chooseModule()
		elif morseTranslations.has_key(morseCode) == False:
			print "No letter matches that code. Try again."
		else:
			letter = morseTranslations[morseCode]
			letters.append(letter)
			for i in xrange(len(morseWords)):
				if letter in morseWords[i]:
					wordsLeft[i] += 1
			wordsLeftCount = 0
			print "Possible words left:"
			print ""
			for i in xrange(len(morseWords)):
				if wordsLeft[i] == count:
					print " ", morseWords[i], ":", morseFreqs[i], "MHz"
					wordsLeftCount += 1
			print ""
			if wordsLeftCount == 1:
				print "You've solved the module!"
				morseCheck = True
			elif wordsLeftCount == 0:
				print "No words are left, start over."
				print ""
				morseCodeModule()
			count += 1
	chooseModule()
	
def memoryModule():
	#Create lists to save data
	buttonPos = []
	buttonNums = []
	possibleNums = ["1","2","3","4"]
	possiblePos = ["first","second","third","fourth"]
	stageCheck = False
	#Stage 1
	stage1 = ["Press the button in the second position","Press the button in the second "
				"position","Press the button in the third position","Press the button in "
				"the fourth position"]
	stage1Pos = [2,2,3,4]
	while stageCheck == False:
		stageCheck = True
		display1 = raw_input("What is the number on the display? : ")
		if display1 == "quit":
			chooseModule()
		if display1 not in possibleNums:
			print "Incorrect input. Try again."
			stageCheck = False
		else:
			print stage1[int(display1) - 1]
			buttonPos.append(stage1Pos[int(display1) - 1])
	stageCheck = False
	while stageCheck == False:
		stageCheck = True
		buttonNum1 = raw_input("What is the number on the button? : ")
		if buttonNum1 == "quit":
			chooseModule()
		if buttonNum1 not in possibleNums:
			print "Incorrect input. Try again."
			stageCheck = False
		else:
			buttonNums.append(int(buttonNum1))
	#Stage 2
	stageCheck = False 
	while stageCheck == False:
		stageCheck = True
		display2 = raw_input("What is the number on the display? : ")
		if display2 == "quit":
			chooseModule()
		if display2 not in possibleNums:
			print "Incorrect input. Try again."
			stageCheck = False
		elif display2 == "1":
			print "Press the button labeled '4'"
			buttonNums.append(4)
			stageCheck = False
			while stageCheck == False:
				stageCheck = True
				position2 = raw_input("What is the position of the button? : ")
				if position2 == "quit":
					chooseModule()
				if position2 not in possibleNums:
					stageCheck = False
					print "Incorrect input. Try again."
				else:
					buttonPos.append(int(position2))
		elif display2 == "2" or display2 == "4":
			print "Push the button in the", possiblePos[buttonPos[0] - 1], "position"
			buttonPos.append(buttonPos[0])
			stageCheck = False
			while stageCheck == False:
				stageCheck = True
				buttonNum2 = raw_input("What is the number on the button? : ")
				if buttonNum2 == "quit":
					chooseModule()
				if buttonNum2 not in possibleNums:
					stageCheck = False
					print "Incorrect input. Try again."
				else:
					buttonNums.append(int(buttonNum2))
		elif display2 == "3":
			print "Push the button in the first position"	
			buttonPos.append(1)
			stageCheck = False
			while stageCheck == False:
				stageCheck = True
				buttonNum2 = raw_input("What is the number on the button? : ")
				if buttonNum2 == "quit":
					chooseModule()
				if buttonNum2 not in possibleNums:
					stageCheck = False
					print "Incorrect input. Try again."
				else:
					buttonNums.append(int(buttonNum2))	
	#Stage 3	
	stageCheck = False 
	while stageCheck == False:
		stageCheck = True
		display3 = raw_input("What is the number on the display? : ")
		if display3 == "quit":
			chooseModule()
		if display3 not in possibleNums:
			print "Incorrect input. Try again."
			stageCheck = False	
		elif display3 == "1" or display3 == "2" or display3 == "3":
			if display3 == "1":
				print "Push the button in the", possiblePos[buttonPos[1] - 1], "position"
				buttonPos.append(buttonPos[1])
			elif display3 == "2":
				print "Push the button in the", possiblePos[buttonPos[0] - 1], "position"
				buttonPos.append(buttonPos[0])
			elif display3 == "3":
				print "Push the button in the third position"
				buttonPos.append(3)
			stageCheck = False
			while stageCheck == False:
				stageCheck = True
				buttonNum3 = raw_input("What is the number on the button? : ")
				if buttonNum3 == "quit":
					chooseModule()
				if buttonNum3 not in possibleNums:
					stageCheck = False
					print "Incorrect input. Try again."
				else:
					buttonNums.append(int(buttonNum3))
		elif display3 == "4":
			print "Press the button labeled '4'"
			buttonNums.append(4)
			stageCheck = False
			while stageCheck == False:
				stageCheck = True
				position3 = raw_input("What is the position of the button? : ")
				if position3 == "quit":
					chooseModule()
				if position3 not in possibleNums:
					stageCheck = False
					print "Incorrect input. Try again."
				else:
					buttonPos.append(int(position3))
	#Stage 4
	stageCheck = False
	while stageCheck == False:
		stageCheck = True
		display4 = raw_input("What is the number on the display? : ")
		if display4 == "quit":
			chooseModule()
		if display4 not in possibleNums:
			print "Incorrect input. Try again."
			stageCheck = False
		else:
			if display4 == "1":
				print "Push the button in the", possiblePos[buttonPos[0] - 1], "position"
				buttonPos.append(buttonPos[0])
			elif display4 == "2":
				print "Push the button in the first position"
				buttonPos.append(1)
			elif display4 == "3"  or display4 == "4":
				print "Push the button in the", possiblePos[buttonPos[1] - 1], "position"
				buttonPos.append(buttonPos[1])
			stageCheck = False
			while stageCheck == False:
				stageCheck = True
				buttonNum4 = raw_input("What is the number on the button? : ")
				if buttonNum4 == "quit":
					chooseModule()
				if buttonNum4 not in possibleNums:
					stageCheck = False
					print "Incorrect input. Try again."
				else:
					buttonNums.append(int(buttonNum4))
	#Stage 5
	stage5Nums = [1,2,4,3]
	stageCheck = False
	while stageCheck == False:
		stageCheck = True
		display5 = raw_input("What is the number on the display? : ")
		if display5 == "quit":
			chooseModule()
		if display5 not in possibleNums:
			print "Incorrect input. Try again."
			stageCheck = False
		else:
			print "Push the button labeled", buttonNums[stage5Nums[int(display5) - 1] - 1]
	chooseModule()
				
def mazeModule():
#Possible directions
	maze1 = [["v>","<>","<v","v>","<>","<"],
			 ["^v","v>","<^","^>","<>","<v"],
			 ["^v","^>","<v","v>","<>","<^v"],
			 ["^v",">","<^>","<^",">","<^v"],
			 ["^v>","<>","<v","v>","<","^v"],
			 ["^>","<","^>","<^",">","<^"]]
	maze2 = [[">","<v>","<","v>","<v>","<"],
			 ["v>","<^","v>","<^","^>","<v"],
			 ["^v","v>","<^","v>","<>","<^v"],
			 ["^v>","<^","v>","<^","v","^v"],
			 ["^v","v","^v","v>","<^","^v"],
			 ["^","^>","<^","^>","<>","<^"]]
	maze3 = [["v>","<>","<v","v","v>","<v"],
			 ["^","v","^v","^>","<^","^v"],
			 ["v>","<^v","^v","v>","<v","^v"],
			 ["^v","^v","^v","^v","^v","^v"],
			 ["^v","^>","<^","^v","^v","^v"],
			 ["^>","<>","<>","<^","^>","<^"]]
	maze4 = [["v>,","<v",">","<>","<>","<v"],
			 ["^v","^v","v>","<>","<>","<^v"],
			 ["^v","^>","<^","v>","<","^v"],
			 ["^v",">","<>","<^>","<>","<^v"],
			 ["^v>","<>","<>","<>","<v","^v"],
			 ["^>","<>","<",">","<^","^"]]
	maze5 = [[">","<>","<>","<>","<v>","<v"],
			 ["v>","<>","<>","<v>","<^","^"],
			 ["^v>","<v",">","<^","v>","<v"],
			 ["^v","^>","<>","<v","^","^v"],
			 ["^v","v>","<>","<^>","<","^v"],
			 ["^","^>","<>","<>","<>","<^"]]
	maze6 = [["v","v>","<v",">","<v>","<v"],
			 ["^v","^v","^v","v>","<^","^v"],
			 ["^>","<^","^","^v","v>","<^"],
			 ["^>","<v","v>","<^v","^v","v"],
			 ["v>","<^","^","^v","^>","<^v"],
			 ["^>","<>","<>","<^",">","<^"]]
	maze7 = [["v>","<>","<>","<v","v>","<v"],
			 ["^v","v>","<","^>","<^","^v"],
			 ["^>","<^","v>","<","v>","<^"],
			 ["v>","<v","^v>","<>","<^","v"],
			 ["^v","^","^>","<>","<v","^v"],
			 ["^>","<>","<>","<>","<^>","<^"]]
	maze8 = [["v","v>","<>","<v","v>","<v"],
			 ["^v>","<^>","<","^>","<^","^v"],
			 ["^v","v>","<>","<>","<v","^v"],
			 ["^v","^>","<v",">","<^>","<^"],
			 ["^v","v","^>","<>","<>","<"],
			 ["^>","<^>","<>","<>","<>","<"]]
	maze9 = [["v","v>","<>","<>","<v>","<v"],
			 ["^v","^v","v>","<","^v","^v"],
			 ["^v>","<^>","<^","v>","<^","^v"],
			 ["^v","v","v>","<^",">","<^v"],
			 ["^v","^v","^v","v>","<v","^"],
			 ["^>","<^","^>","<^","^>","<"]]
	possibleCoords = ["1","2","3","4","5","6"]
	startRow = 0
	startCol = 0
	row = 0
	col = 0
	endRow = 0
	endCol = 0
	prevRow = -1
	prevCol = -1
	prevSplitRow = -1 #The last place where you had to branch
	prevSplitCol = -1
	directions = []
	maze = []
	deadEndRows = []
	deadEndCols = []
	mazeCheck = False
	#Determine which maze
	circle = raw_input("Enter coordinates of one of the circular markings : ")
	if circle == "quit":
		chooseModule()
	elif len(circle) != 2 or circle.isdigit() == False:
		print "Incorrect input. Try again. Form : xy (ex. : 23)"
		mazeModule()
	elif circle[0] not in possibleCoords or circle[1] not in possibleCoords:
		print "Coordinates not in maze (1-6). Try again"
		mazeModule()
	elif circle == "12" or circle == "63":
		maze = maze1
	elif circle == "24" or circle == "52":
		maze = maze2
	elif circle == "44" or circle == "64":
		maze = maze3
	elif circle == "11" or circle == "14":
		maze = maze4
	elif circle == "46" or circle == "53":
		maze = maze5
	elif circle == "35" or circle == "51":
		maze = maze6
	elif circle == "21" or circle == "26":
		maze = maze7
	elif circle == "34" or circle == "41":
		maze = maze8
	elif circle == "15" or circle == "32":
		maze = maze9
	else:
		print "Not a marking location in any of the mazes. Try again."
		mazeModule()
	#Ascertain start and end locations
	while mazeCheck == False:
		mazeCheck = True
		startLoc = raw_input("Enter coordinates of white light : ")
		if startLoc == "quit":
			chooseModule()
		elif len(startLoc) != 2 or startLoc.isdigit() == False:
			print "Incorrect input. Try again. Form : xy (ex. : 23)"
			mazeCheck = False
		elif startLoc[0] not in possibleCoords or startLoc[1] not in possibleCoords:
			print "Coordinates not in maze (1-6). Try again"
			mazeCheck = False
		else:
			startRow = int(startLoc[1]) - 1
			row = int(startLoc[1]) - 1
			startCol = int(startLoc[0]) - 1
			col = int(startLoc[0]) - 1
	mazeCheck = False
	while mazeCheck == False:
		mazeCheck = True
		endLoc = raw_input("Enter coordinates of red triangle : ")
		if endLoc == "quit":
			chooseModule()
		elif len(endLoc) != 2 or endLoc.isdigit() == False:
			print "Incorrect input. Try again. Form : xy (ex. : 23)"
			mazeCheck = False
		elif endLoc[0] not in possibleCoords or endLoc[1] not in possibleCoords:
			print "Coordinates not in maze (1-6). Try again"
			mazeCheck = False
		else:
			endRow = int(endLoc[1]) - 1
			endCol = int(endLoc[0]) - 1
	#Making a move
	while row != endRow or col != endCol: 
	#Finding the number of possible moves from current space
		length = len(maze[row][col])
		currentPos = maze[row][col]    #Dummy copy so we can delete unavailable moves 
	#Checking for unavailable moves			
		if "<" in maze[row][col]:
			for i in xrange(len(deadEndRows)):
				if row == deadEndRows[i] and (col - 1) == deadEndCols[i]:
					length -= 1
					currentPos = currentPos.replace("<","")
			if row == prevRow and (col - 1) == prevCol:
				length -= 1
				currentPos = currentPos.replace("<","")
		if ">" in maze[row][col]:
			for i in xrange(len(deadEndRows)):
				if row == deadEndRows[i] and (col + 1) == deadEndCols[i]:
					length -= 1
					currentPos = currentPos.replace(">","")
			if row == prevRow and (col + 1) == prevCol:
				length -= 1
				currentPos = currentPos.replace(">","")
		if "v" in maze[row][col]:
			for i in xrange(len(deadEndRows)):
				if (row + 1) == deadEndRows[i] and col == deadEndCols[i]:
					length -= 1
					currentPos = currentPos.replace("v","")
			if (row + 1) == prevRow and col == prevCol:
				length -= 1
				currentPos = currentPos.replace("v","")
		if "^" in maze[row][col]:
			for i in xrange(len(deadEndRows)):
				if (row - 1) == deadEndRows[i] and col == deadEndCols[i]:
					length -= 1
					currentPos = currentPos.replace("^","")
			if (row - 1) == prevRow and col == prevCol:
				length -= 1
				currentPos = currentPos.replace("^","")
	#Making a move
		if length == 0:
				deadEndRows.append(prevSplitRow)   	#Dead End Case
				deadEndCols.append(prevSplitCol)
				directions = [] 					#Reset directions
				row = startRow
				col = startCol
				prevRow = 0
				prevCol = 0
				prevSplitRow = -1
				prevSplitCol = -1 
		if length == 1:
			prevRow = row
			prevCol = col
			if currentPos == "<":
				col -= 1
				directions.append("left")
			elif currentPos == ">":
				col += 1
				directions.append("right")
			elif currentPos == "v":
				row += 1
				directions.append("down")
			elif currentPos == "^":
				row -= 1
				directions.append("up")
		if length == 2 or length == 3:
			choice = randint(0,(length - 1))
			prevRow = row
			prevCol = col
			if currentPos[choice] == "<":
				col -= 1
				directions.append("left")
			elif currentPos[choice] == ">":
				col += 1
				directions.append("right")
			elif currentPos[choice] == "v":
				row += 1
				directions.append("down")
			elif currentPos[choice] == "^":
				row -= 1
				directions.append("up")        
			prevSplitRow = row
			prevSplitCol = col
	print "Directions :"		
	print ""
	print directions
	print ""
	chooseModule()
	
def passwordModule(): 
#Creating base arrays
	passwords = ["about","after","again","below","could","every","first","found","great",
				 "house","large","learn","never","other","place","plant","point","right",
				 "small","sound","spell","still","study","their","there","these","thing",
				 "think","three","water","where","which","world","would","write"]
	passwordsLeft = []
	print "All passwords: \n"
	leftCount = 0
	for i in xrange(len(passwords)):
		passwordsLeft.append(0) # 1 = still possible, 0 = not possible
#Eliminating until one word is left
#First letter
	firstLetter = raw_input("Enter possible first letters: ").lower()
	if firstLetter == "quit":
		chooseModule()
	for i in xrange(len(passwords)):
		for j in xrange(len(firstLetter)):
			if firstLetter[j] == passwords[i][0]:
				passwordsLeft[i] = 1 #Exclusive list of passwords left
	print "Passwords left:"
	for i in xrange(len(passwords)):
		if passwordsLeft[i] == 1:
			print passwords[i],
			leftCount += 1
	print ""
#Exit Cases		
	if leftCount == 1:
		chooseModule()
	if leftCount == 0:
		print "You entered something incorrect, try again"
		passwordModule()
#Second Letter
	leftCount = 0
	secondLetter = raw_input("Enter possible second letters: ").lower()
	if secondLetter == "quit":
		chooseModule()
	for i in xrange(len(passwords)):
		for j in xrange(len(secondLetter)):
			if secondLetter[j] == passwords[i][1] and passwordsLeft[i] == 1:
				passwordsLeft[i] = 2 #Exclusive list of passwords left
	print "Passwords left:"
	for i in xrange(len(passwords)):
		if passwordsLeft[i] == 2:
			print passwords[i],
			leftCount += 1
	print ""
#Exit Cases		
	if leftCount == 1:
		print "You figured out the password!"
		chooseModule()
	if leftCount == 0:
		print "You entered something incorrect, try again"
		passwordModule()
#Third Letter
	leftCount = 0
	thirdLetter = raw_input("Enter possible third letters: ").lower()
	if thirdLetter == "quit":
		chooseModule()
	for i in xrange(len(passwords)):
		for j in xrange(len(thirdLetter)):
			if thirdLetter[j] == passwords[i][2] and passwordsLeft[i] == 2:
				passwordsLeft[i] = 3 #Exclusive list of passwords left
	print "Passwords left:"
	for i in xrange(len(passwords)):
		if passwordsLeft[i] == 3:
			print passwords[i],
			leftCount += 1
	print ""
#Exit Cases		
	if leftCount == 1:
		print "You figured out the password!"
		chooseModule()
	if leftCount == 0:
		print "You entered something incorrect, try again"
		passwordModule()
#Fourth Letter
	leftCount = 0
	fourthLetter = raw_input("Enter possible fourth letters: ").lower()
	if fourthLetter == "quit":
		chooseModule()
	for i in xrange(len(passwords)):
		for j in xrange(len(fourthLetter)):
			if fourthLetter[j] == passwords[i][3] and passwordsLeft[i] == 3:
				passwordsLeft[i] = 4 #Exclusive list of passwords left
	print "Passwords left:"
	for i in xrange(len(passwords)):
		if passwordsLeft[i] == 4:
			print passwords[i],
			leftCount += 1
	print ""
#Exit Cases		
	if leftCount == 1:
		print "You figured out the password!"
		chooseModule()
	if leftCount == 0:
		print "You entered something incorrect, try again"
		passwordModule()
#Fifth Letter
	leftCount = 0
	fifthLetter = raw_input("Enter possible fifth letters: ").lower()
	if fifthLetter == "quit":
		chooseModule()
	for i in xrange(len(passwords)):
		for j in xrange(len(fifthLetter)):
			if fifthLetter[j] == passwords[i][4] and passwordsLeft[i] == 4:
				passwordsLeft[i] = 5 #Exclusive list of passwords left
	print "Final password:"
	for i in xrange(len(passwords)):
		if passwordsLeft[i] == 5:
			print passwords[i],
			leftCount += 1
	print ""
#Exit Cases		
	if leftCount == 1:
		print "You figured out the password!"
		chooseModule()
	if leftCount == 0 or leftCount > 1:
		print "You entered something incorrect, try again"
		passwordModule()						
	chooseModule()

	#Needy Modules
	
def knobsModule():
#Fastest way for this module is just to see the options
	print "Up Position:"
	print "001011      101010"
	print "111101      011011"
	print ""
	print "Down Position:"
	print "011001      101010"
	print "111101      010001"
	print ""
	print "Left Position:"
	print "000010      000010"
	print "100111      000110"
	print ""
	print "Right Position:"
	print "101111      101100"
	print "111010      111010"
	print ""
	chooseModule()
	
		
#Start of program
chooseModule()	
