#! /usr/bin/python3

import re, os
from datetime import datetime
from datetime import timedelta

os.chdir('/home/john/Videos/SubtitleMod')


#set the file name equal to the first .srt file it finds in the directory

#CREATE TWO SEPARATE FUNCTIONS, one for addition one for subtraction
#the addition will require timedelta and different formatting for the string replacement

def hasten():

	files = os.listdir()

	for i in range(len(files)):
		if 'output_' not in files[i] and files[i].endswith('.srt') == True:
			inputFileName = files[i]
			inputFile = open(files[i])
			content = inputFile.read()
			break

	#establish the regex search and create list
	timeRegex = re.compile(r'\d\d:\d\d:\d\d,\d\d\d')
	origTimes = timeRegex.findall(content)
	origTimes

	minutes = input('Minutes: ')
	seconds = input('Seconds: ')
	td = timedelta(minutes = int(minutes), seconds = int(seconds))

	#create list of new times
	newTimes = []
	for origTime in origTimes:
		#if no microseonds, doesn't work... add microseconds
		if origTime[-3:] == '000':
			origTimeMod = origTime[:9] + '001'
		else:
			origTimeMod = origTime

		to = datetime.strptime(origTimeMod, '%H:%M:%S,%f')
		newTime = to - td
		no = str(newTime).replace('.',',')[11:23]
		newTimes.append(no)

	#now search through file, wherever I find
	for i in range(len(origTimes)):
		content = content.replace(origTimes[i],newTimes[i])

	inputFile.close()
	#outputFile = open('output_' + inputFile ,'w')


	outputFile = open('output_' + os.listdir()[0] ,'w')
	outputFile.write(content)
	outputFile.close()

	print('Output filename:  output_' + os.listdir()[0])

def delay():
	print('This isn\'t ready yet')
	files = os.listdir()

	for i in range(len(files)):
		if 'output_' not in files[i]:
			inputFileName = files[i]
			inputFile = open(files[i])
			content = inputFile.read()
			break

	#establish the regex search and create list
	timeRegex = re.compile(r'\d\d:\d\d:\d\d,\d\d\d')
	origTimes = timeRegex.findall(content)
	origTimes

	minutes = input('Minutes: ')
	seconds = input('Seconds: ')
	td = timedelta(minutes = int(minutes), seconds = int(seconds))

	#create list of new times
	newTimes = []
	for origTime in origTimes: #do I need to reversed this?
		#if no microseonds, doesn't work... add microseconds
		if origTime[-3:] == '000':
			origTimeMod = origTime[:9] + '001'
		else:
			origTimeMod = origTime

		to = datetime.strptime(origTimeMod, '%H:%M:%S,%f')
		newTime = to + td
		no = str(newTime).replace('.',',')[11:23]
		newTimes.append(no)


	#reverse the lists so I don't find a time twice (because I'm adding)
	newTimes = list(reversed(newTimes))
	origTimes = list(reversed(origTimes))

	#replace old time with new time
	for i in range(len(origTimes)):
		content = content.replace(origTimes[i],newTimes[i])
	inputFile.close()

	outputFile = open('output_' + os.listdir()[0] ,'w')
	outputFile.write(content)
	outputFile.close()

	print('Output filename:  output_' + os.listdir()[0])


selection = input('(H)asten or (D)elay?:  ')
if selection.upper() == 'H':
	hasten()
elif selection.upper() == 'D':
	delay()
