'''
Part II - Write to CSV File

Q5. Write email addresses from Part I to csv file

Place your code in this file: advanced_python_csv.py

The emails.csv file you create should be added and committed to your forked
repository.

Your file, emails.csv, will look like this:

bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
'''



# PLACE YOUR CODE HERE

import csv

# open the file, convert it to first a csv reader object, then a list
f = open('faculty.csv', 'r')
r = csv.reader(f)
l = list(r)

# remove the header entry
header = l.pop(0)

# the following code snippet is from my answer in advanced_python_regex.py:

# let's find the index for the email column
for col in range(len(header)):
	if header[col] == ' email':
		email_i = col
		break

# let's make a list
emailList = []

for entry in l:
	# get the email address
	currentEmail = entry[email_i]
	emailList.append(currentEmail)

# so now we have the list of emails

# create a new file in write mode
newfile = open('emails.csv', 'w')

# traverse through emailList 
for email in emailList:
	# write each email to the file with a newline char
	newfile.write(email + ',\n')

# not sure if this is necessary here?
newfile.close()


