'''
Q1. Find how many different degrees there are, and their frequencies: 
	Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

REPLACE THIS WITH YOUR RESPONSE
Q2. Find how many different titles there are, and their frequencies:
	Ex: Assistant Professor, Professor

REPLACE THIS WITH YOUR RESPONSE
Q3. Search for email addresses and put them in a list. Print the list of 
	email addresses.

REPLACE THIS WITH YOUR RESPONSE
Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, 
	upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.

REPLACE THIS WITH YOUR RESPONSE
'''

# PLACE YOUR CODE HERE

import csv

# open the file, convert it to first a csv reader object, then a list
f = open('faculty.csv', 'r')
r = csv.reader(f)
l = list(r)

# remove the header entry
header = l.pop(0)

# let's find the indices for each column
# the space in front of the latter three in this for statement is a product
#  of the file itself, this may cause problems later but we'll jump that hurdle
#  when we get to it
for col in range(len(header)):
	if header[col] == 'name':
		name_i = col
		next
	if header[col] == ' degree':
		degree_i = col
		next
	if header[col] == ' title':
		title_i = col
		next
	if header[col] == ' email':
		email_i = col

# Q1. Find how many different degrees there are, and their frequencies: 
#	Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

# let's make a dictionary
degreeDict = {}

for entry in l:
	# get the degree
	currentDegree = entry[degree_i]
	# we remove all periods and change everything to uppercase
	currentDegree = currentDegree.replace('.', '')
	currentDegree = currentDegree.upper()
	# now we use str.split() to split it into a list, thus removing all spaces
	#  (leading or otherwise)
	currentDegree = currentDegree.split()

	for deg in currentDegree:
		# check to see if the entry is already in the dictionary
		if deg in degreeDict:
			degreeDict[deg] = degreeDict[deg] + 1
		# otherwise, add a new entry, with 1 as the value
		else:
			degreeDict[deg] = 1

print(degreeDict)
# {'MA': 1, 'MS': 2, 'PHD': 31, 'MD': 1, 'BSED': 1, 'SCD': 6, 'MPH': 2, 
#	'0': 1, 'JD': 1}


# Q2. Find how many different titles there are, and their frequencies:
#	Ex: Assistant Professor, Professor

# let's make a dictionary
titleDict = {}

# I could probably combine this with the first for statement, but for the sake
#  of this assignment, I'll seperate them to seperate my work for each question
for entry in l:
	# get the title
	currentTitle = entry[title_i]
	# change everything to uppercase and remove " OF BIOSTATISTICS"
	currentTitle = currentTitle.upper()
	currentTitle = currentTitle.replace(' OF BIOSTATISTICS', '')
	# ... and remove the one instance of ' IS BIOSTATISTICS'
	currentTitle = currentTitle.replace(' IS BIOSTATISTICS', '')

	'''
	for deg in currentDegree:
		# check to see if the entry is already in the dictionary
		if deg in degreeDict:
			degreeDict[deg] = degreeDict[deg] + 1
		# otherwise, add a new entry, with 1 as the value
		else:
			degreeDict[deg] = 1
	'''

	# check to see if the entry is already in the dictionary
	if currentTitle in titleDict:
		titleDict[currentTitle] = titleDict[currentTitle] + 1
	# otherwise, add a new entry, with 1 as the value
	else:
		titleDict[currentTitle] = 1

print(titleDict)
# {'ASSOCIATE PROFESSOR': 12, 'PROFESSOR': 13, 'ASSISTANT PROFESSOR': 12}


# Q3. Search for email addresses and put them in a list. Print the list of 
#	email addresses.

# let's make a list
emailList = []

for entry in l:
	# get the email address
	currentEmail = entry[email_i]
	emailList.append(currentEmail)

print(emailList)
# ['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu', 
#	'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.upenn.edu',
#	'ruifeng@upenn.edu', 'bcfrench@mail.med.upenn.edu', 'pgimotty@upenn.edu',
#	'wguo@mail.med.upenn.edu', 'hsu9@mail.med.upenn.edu',
#	'rhubb@mail.med.upenn.edu', 'whwang@mail.med.upenn.edu',
#	'mjoffe@mail.med.upenn.edu', 'jrlandis@mail.med.upenn.edu',
#	'liy3@email.chop.edu', 'mingyao@mail.med.upenn.edu', 'hongzhe@upenn.edu',
#	'rlocalio@upenn.edu', 'nanditam@mail.med.upenn.edu', 
#	'knashawn@mail.med.upenn.edu', 'propert@mail.med.upenn.edu', 
#	'mputt@mail.med.upenn.edu', 'sratclif@upenn.edu', 'michross@upenn.edu',
#	'jaroy@mail.med.upenn.edu', 'msammel@cceb.med.upenn.edu',
#	'shawp@upenn.edu', 'rshi@mail.med.upenn.edu', 'hshou@mail.med.upenn.edu',
#	'jshults@mail.med.upenn.edu', 'alisaste@mail.med.upenn.edu',
#	'atroxel@mail.med.upenn.edu', 'rxiao@mail.med.upenn.edu',
#	'sxie@mail.med.upenn.edu', 'dxie@upenn.edu', 'weiyang@mail.med.upenn.edu']


# Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, 
#	upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.

# this builds off of the list made for the Q3 section, so refer to that for
#  creation of the email list

# let's create a dictionary
domainDict = {}

for address in emailList:
	# cleaning up the string
	currentDomain = address
	# remove the '@' and everything preceeding it
	ampIndex = currentDomain.find('@')
	currentDomain = currentDomain[ampIndex+1:]

	# check to see if the entry is already in the dictionary
	if currentDomain in domainDict:
		domainDict[currentDomain] = domainDict[currentDomain] + 1
	# otherwise, add a new entry, with 1 as the value
	else:
		domainDict[currentDomain] = 1

print(domainDict)
# {'email.chop.edu': 1, 'cceb.med.upenn.edu': 1, 'upenn.edu': 12, 'mail.med.upenn.edu': 23}






