# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 
# goals against opponents, and had 36 goals scored against them). Write a
# program to read the file, then print the name of the team with the smallest
# difference in ‘for’ and ‘against’ goals.

import csv

# open the file, convert it to first a csv reader object, then a list
f = open('football.csv', 'r')
r = csv.reader(f)
l = list(r)

# remove the header entry
header = l.pop(0)

# goals are in index 5 and goals allowed are in index 6 in the original csv,
#  but let's see if we find it without prior knowledge of which rows they're
#  in
for col in range(len(header)):
	if header[col] == 'Team':
		teamname = col
		next
	if header[col] == 'Goals':
		goals = col
		next
	if header[col] == 'Goals Allowed':
		goals_allowed = col


# makes a list of two element lists by parsing out each team name followed by 
#  that team's goals-goals allowed
goal_diff_list = []
for team in l:
	goal_diff_list.append( [ team[teamname], 
				int(team[goals])-int(team[goals_allowed]) ] )

# now to sort by goal difference (lowest goal difference should be element 0)
sorted_goal_diff = sorted(goal_diff_list, key = lambda x: x[-1])

print(sorted_goal_diff[0][0])
# poor Leicester, at least they got their title in the 15-16 season
