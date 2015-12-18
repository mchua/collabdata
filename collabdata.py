import csv

with open('collabdata.csv', 'r') as f:
	reader = csv.reader(f)
	data = list(reader)

# Visitor class
class Visitor(object):
	def __init__(self, idno, name, org, jobtitle, email):
		self.idno = idno # integer ID number
		self.name = name
		self.org = org   # integer org number
		self.jobtitle = jobtitle
		self.email = email
		self.visits = []

# Empty storage for visitors, orgs
visitors = {}
orgs = {}
##TODO: Create and populate a list for visits

repeats = 0

for visit in data[1:]: # skip first row of header info
	if int(visit[0]) not in visitors: # new person
		idno = int(visit[0])
		name = visit[1].rstrip() ##TODO: strip whitespace on input parse
		org = int(visit[13])
		jobtitle = visit[15].rstrip() ##TODO: strip whitespace on input parse
		email = visit[9].rstrip()
		visitors[idno] = Visitor(idno, name, org, jobtitle, email)
		##TODO: move initialization to Visitor init function
		##TODO: add an Org object that's similar
		##TODO: add a Visit object that's similar
	else:
		repeats = repeats +1

print(len(visitors)) 	##RESULT: unique visitors
print(repeats)		##RESULT: visits from people who've visited Olin before
print(len(visitors)+repeats)	##TEST: should be the same length
				## 	as original spreadsheet

##TODO: This is a test for stripping whitespace on input
##	When whitespace is skipped on input, the two print statements
##	will have the same value
print(len(data[1834][1]))
print(len(visitors[99459346].name))

##TEST:
print(visitors[99459346].name)
