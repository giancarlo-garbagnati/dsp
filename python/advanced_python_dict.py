'''
Part III - Dictionary

Q6. Create a dictionary in the below format:

faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], 
				['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
Print the first 3 key and value pairs of the dictionary:

REPLACE THIS WITH YOUR RESPONSE
Q7. The previous dictionary does not have the best design for keys. Create
a new dictionary with keys as:

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor',
	'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor',
	'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.',
	'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'):
	['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
	('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
Print the first 3 key and value pairs of the dictionary:

REPLACE THIS WITH YOUR RESPONSE
Q8. It looks like the current dictionary is printing by first name. Print 
out the dictionary key value pairs based on alphabetical orders of the last 
name of the professors

REPLACE THIS WITH YOUR RESPONSE
'''


# so it looks like our keys are a string, and the value is a list of lists
#  where the outer list represents all the people with the same last name
#  and each internal list contains the information (degree, title, email)

# let's steal some more of my code from advanced_python_regex.py:

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

# now let's do something a little differently, let's seperate the main list
#  into each column, so each index represents one person/entry
# we'll include the entry cleaning in this loop as well
nameList = []
firstNameList = []
lastNameList = []
degreeList = []
titleList = []
emailList = []

for entry in l:

	# name lists (full, first, last)
	name = entry[name_i]
	nameList.append(name)

	# some entries have an initialism for the first name in their full name,
	#  I'm not entirely sure how this excercise expects us to handle it
	#  so I'll just take it as their first name
	#  for example 'J. Richard Landis' becomes first name 'J.' and last name
	#  'Landis', and we'll ignore 'Richard' in the context of first/last
	#  names
	firstNameList.append(name.split()[0])
	lastNameList.append(name.split()[-1])

	# list of degrees
	degree = entry[degree_i]
	# need to clean any leading ' 's
	if degree[0] == ' ':
		degree = degree[1:]
	# otherwise as I understand for this assignment, we won't need to split
	#  up all the degrees
	degreeList.append(degree)

	# title list
	title = entry[title_i]
	# now we clean up anything after the substring 'Professor'
	profStr = 'Professor'
	prof_i = title.find(profStr) + len(profStr)
	# now we have an index for the end of 'Professor' and we can add
	#  everything preceeding to the list
	titleList.append(title[:prof_i])

	# email list
	# this should be straightforward
	emailList.append(entry[email_i])

# a set of checks to see if each list is the same length
#print(len(nameList))
#print(len(firstNameList))
#print(len(lastNameList))
#print(len(degreeList))
#print(len(titleList))
#print(len(emailList))


# so all the lists should be made


'''
Q6. Create a dictionary in the below format:

faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], 
				['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
Print the first 3 key and value pairs of the dictionary:
'''

# let's create a dictionary
faculty_dict = {}

# now let's go through with making the first dictionary
for i in range(len(nameList)):
	#currLastName = lastNameList[i]
	#currDegree = degreeList[i]
	#currTitle = titleList[i]
	#currEmail = emailList[i]

	key = lastNameList[i]
	valueElement = [degreeList[i], titleList[i], emailList[i]]

	# check to see if the entry is already in the dictionary, and if so will
	#  append to the current dictionary
	if key in faculty_dict:
		faculty_dict[key].append(valueElement)
	# otherwise, add a new entry, valueElement as the value
	else:
		faculty_dict[key] = [valueElement]


print("**********Q6**********")
# is there a better way to do this in py3?
for i in range(3):
	print(list(faculty_dict.items())[i])
# ('Xie', [['Ph.D.', 'Associate Professor', 'sxie@mail.med.upenn.edu'], 
#	['PhD', 'Assistant Professor', 'dxie@upenn.edu']])
# ('Bilker', [['Ph.D.', 'Professor', 'warren@upenn.edu']])
# ('French', [['PhD', 'Associate Professor', 'bcfrench@mail.med.upenn.edu']])

# although this changes each time you make the dictionary


'''
Q7. The previous dictionary does not have the best design for keys. Create
a new dictionary with keys as:

professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor',
	'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor',
	'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.',
	'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'):
	['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],
	('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
Print the first 3 key and value pairs of the dictionary:
'''

# let's create another dictionary
professor_dict = {}

# this can probably have been done in that loop above, but we'll just make
#  a new loop for the sake of seperating the work for each question in this
#  assignment

for i in range(len(nameList)):

	key = (firstNameList[i], lastNameList[i])
	valueElement = [degreeList[i], titleList[i], emailList[i]]

	# we shouldn't need to check for if the item exists, because each item
	#  should be unique
	professor_dict[key] = valueElement


print("**********Q7**********")
for i in range(3):
	print(list(professor_dict.items())[i])
# (('Yimei', 'Li'), ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'])
# (('J.', 'Landis'), ['B.S.Ed. M.S. Ph.D.', 'Professor', 
#	'jrlandis@mail.med.upenn.edu'])
# (('Alisa', 'Stephens'), ['Ph.D.', 'Assistant Professor', 
#	'alisaste@mail.med.upenn.edu'])

# although this changes each time you make the dictionary


'''
Q8. It looks like the current dictionary is printing by first name. Print 
out the dictionary key value pairs based on alphabetical orders of the last 
name of the professors
'''

# make a list of the name tuples
# make a list of the last name
# ???
# profit

# let's make lists of tuples made from the keys of the professor_dict
#  dictionary, then let's make another dictionary from switching the two
#  names
firstLast = list(professor_dict.keys())
lastFirst = []

# making a new list of tuples with swapped names
for element in firstLast:
	lastFirst.append((element[1],element[0]))

# now we sort
lastFirst = sorted(lastFirst)

print("**********Q8 pt1**********")
# printing just the first 3 key value pairs
for i in range(3):
	f = lastFirst[i][1]
	l = lastFirst[i][0]
	fl = (f, l)
	value = professor_dict.get(fl)
	print(fl, value)
'''
('Scarlett', 'Bellamy') ['Sc.D.', 'Associate Professor', 'bellamys@mail.med.upenn.edu']
('Warren', 'Bilker') ['Ph.D.', 'Professor', 'warren@upenn.edu']
('Matthew', 'Bryan') ['PhD', 'Assistant Professor', 'bryanma@upenn.edu']
'''

print("**********Q8 pt2**********")
# printing all the key value pairs
for i in range(len(lastFirst)):
	f = lastFirst[i][1]
	l = lastFirst[i][0]
	fl = (f, l)
	value = professor_dict.get(fl)
	print(fl, value)
'''
('Scarlett', 'Bellamy') ['Sc.D.', 'Associate Professor', 'bellamys@mail.med.upenn.edu']
('Warren', 'Bilker') ['Ph.D.', 'Professor', 'warren@upenn.edu']
('Matthew', 'Bryan') ['PhD', 'Assistant Professor', 'bryanma@upenn.edu']
('Jinbo', 'Chen') ['Ph.D.', 'Associate Professor', 'jinboche@upenn.edu']
('Jonas', 'Ellenberg') ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
('Susan', 'Ellenberg') ['Ph.D.', 'Professor', 'sellenbe@upenn.edu']
('Rui', 'Feng') ['Ph.D', 'Assistant Professor', 'ruifeng@upenn.edu']
('Benjamin', 'French') ['PhD', 'Associate Professor', 'bcfrench@mail.med.upenn.edu']
('Phyllis', 'Gimotty') ['Ph.D', 'Professor', 'pgimotty@upenn.edu']
('Wensheng', 'Guo') ['Ph.D', 'Professor', 'wguo@mail.med.upenn.edu']
('Yenchih', 'Hsu') ['Ph.D.', 'Assistant Professor', 'hsu9@mail.med.upenn.edu']
('Rebecca', 'Hubbard') ['PhD', 'Associate Professor', 'rhubb@mail.med.upenn.edu']
('Wei-Ting', 'Hwang') ['Ph.D.', 'Associate Professor', 'whwang@mail.med.upenn.edu']
('Marshall', 'Joffe') ['MD MPH Ph.D', 'Professor', 'mjoffe@mail.med.upenn.edu']
('J.', 'Landis') ['B.S.Ed. M.S. Ph.D.', 'Professor', 'jrlandis@mail.med.upenn.edu']
('Hongzhe', 'Li') ['Ph.D', 'Professor', 'hongzhe@upenn.edu']
('Mingyao', 'Li') ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu']
('Yimei', 'Li') ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu']
('A.', 'Localio') ['JD MA MPH MS PhD', 'Associate Professor', 'rlocalio@upenn.edu']
('Nandita', 'Mitra') ['Ph.D.', 'Associate Professor', 'nanditam@mail.med.upenn.edu']
('Knashawn', 'Morales') ['Sc.D.', 'Associate Professor', 'knashawn@mail.med.upenn.edu']
('Kathleen', 'Propert') ['Sc.D.', 'Professor', 'propert@mail.med.upenn.edu']
('Mary', 'Putt') ['PhD ScD', 'Professor', 'mputt@mail.med.upenn.edu']
('Sarah', 'Ratcliffe') ['Ph.D.', 'Associate Professor', 'sratclif@upenn.edu']
('Michelle', 'Ross') ['PhD', 'Assistant Professor', 'michross@upenn.edu']
('Jason', 'Roy') ['Ph.D.', 'Associate Professor', 'jaroy@mail.med.upenn.edu']
('Mary', 'Sammel') ['Sc.D.', 'Professor', 'msammel@cceb.med.upenn.edu']
('Pamela', 'Shaw') ['PhD', 'Assistant Professor', 'shawp@upenn.edu']
('Russell', 'Shinohara') ['0', 'Assistant Professor', 'rshi@mail.med.upenn.edu']
('Haochang', 'Shou') ['Ph.D.', 'Assistant Professor', 'hshou@mail.med.upenn.edu']
('Justine', 'Shults') ['Ph.D.', 'Professor', 'jshults@mail.med.upenn.edu']
('Alisa', 'Stephens') ['Ph.D.', 'Assistant Professor', 'alisaste@mail.med.upenn.edu']
('Andrea', 'Troxel') ['ScD', 'Professor', 'atroxel@mail.med.upenn.edu']
('Rui', 'Xiao') ['PhD', 'Assistant Professor', 'rxiao@mail.med.upenn.edu']
('Dawei', 'Xie') ['PhD', 'Assistant Professor', 'dxie@upenn.edu']
('Sharon', 'Xie') ['Ph.D.', 'Associate Professor', 'sxie@mail.med.upenn.edu']
('Wei', 'Yang') ['Ph.D.', 'Assistant Professor', 'weiyang@mail.med.upenn.edu']
'''


