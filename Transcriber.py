#
#  Transcriber.py
#  Rubik's Cube Solver
#
#  Created by Blake Williams on 1/10/19.
#  Copyright © 2019 Blake Williams. All rights reserved.
#


import copy
def RealMovesOnly(history):
	# move : actual motor
	dicXC={'UC':'FC','UCC':'FCC','DC':'BC',
	'DCC':'BCC','LC':'LC','LCC':'LCC',
	'RC':'RC','RCC':'RCC','FC':'DC',
	'FCC':'DCC','BC':'UC','BCC':'UCC',
	'XC':'XC','XCC':'XCC','YC':'ZC',
	'YCC':'ZCC','ZC':'YCC','ZCC':'YC'}

	dicXCC={'UC':'BC','UCC':'BCC','DC':'FC',
	'DCC':'FCC','LC':'LC','LCC':'LCC',
	'RC':'RC','RCC':'RCC','FC':'UC',
	'FCC':'UCC','BC':'DC','BCC':'DCC',
	'XC':'XC','XCC':'XCC','YC':'ZCC',
	'YCC':'ZC','ZC':'YC','ZCC':'YCC'}

	dicYC={'UC':'UC','UCC':'UCC','DC':'DC',
	'DCC':'DCC','LC':'FC','LCC':'FCC',
	'RC':'BC','RCC':'BCC','FC':'RC',
	'FCC':'RCC','BC':'LC','BCC':'LCC',
	'XC':'ZCC','XCC':'ZC','YC':'YC',
	'YCC':'YCC','ZC':'XC','ZCC':'XCC'}

	dicYCC={'UC':'UC','UCC':'UCC','DC':'DC',
	'DCC':'DCC','LC':'BC','LCC':'BCC',
	'RC':'FC','RCC':'FCC','FC':'LC',
	'FCC':'LCC','BC':'RC','BCC':'RCC',
	'XC':'ZC','XCC':'ZCC','YC':'YC',
	'YCC':'YCC','ZC':'XCC','ZCC':'XC'}

	dicZC={'UC':'LC','UCC':'LCC','DC':'RC',
	'DCC':'RCC','LC':'DC','LCC':'DCC',
	'RC':'UC','RCC':'UCC','FC':'FC',
	'FCC':'FCC','BC':'BC','BCC':'BCC',
	'XC':'YC','XCC':'YCC','YC':'XCC',
	'YCC':'XC','ZC':'ZC','ZCC':'ZCC'}

	dicZCC={'UC':'RC','UCC':'RCC','DC':'LC',
	'DCC':'LCC','LC':'UC','LCC':'UCC',
	'RC':'DC','RCC':'DCC','FC':'FC',
	'FCC':'FCC','BC':'BC','BCC':'BCC',
	'XC':'YCC','XCC':'YC','YC':'XC',
	'YCC':'XCC','ZC':'ZC','ZCC':'ZCC'}

	hisCopy = copy.deepcopy(history)
	size = len(hisCopy)
	for i in range(size):
		if hisCopy[i] == 'XC':
			for x in range(i+1,size):
				hisCopy[x]=dicXC[hisCopy[x]]
		elif hisCopy[i] == 'XCC':
			for x in range(i+1,size):
				hisCopy[x]=dicXCC[hisCopy[x]]
		elif hisCopy[i] == 'YC':
			for x in range(i+1,size):
				hisCopy[x]=dicYC[hisCopy[x]]
		elif hisCopy[i] == 'YCC':
			for x in range(i+1,size):
				hisCopy[x]=dicYCC[hisCopy[x]]
		elif hisCopy[i] == 'ZC':
			for x in range(i+1,size):
				hisCopy[x]=dicZC[hisCopy[x]]
		elif hisCopy[i] == 'ZCC':
			for x in range(i+1,size):
				hisCopy[x]=dicZCC[hisCopy[x]]

	undesireables = ['XC','XCC','YC','YCC','ZC','ZCC']
	movesOnly = []
	for i in hisCopy:
		if i in undesireables:
			pass
		else:
			movesOnly.append(i)
	return movesOnly

def Compress(history):
	i=0
	while i < len(history)-1:
		change = True
		while change and i < len(history)-1:
			equiv1 = history[i] == history[i+1]
			if len(history)-i>=3:
				equiv2 = history[i] == history[i+2]
			else:
				equiv2 = False
			if len(history)-i >=4:
				equiv3 = history[i] == history[i+3]
			else:
				equiv3 = False
			if equiv1 and equiv2 and equiv3:
				del history[i]
				del history[i]
				del history[i]
				del history[i]

			elif history[i][0] == history[i+1][0] and not equiv1:
				del history[i]
				del history[i]

			elif equiv1 and equiv2:
				if len(history[i]) == 2:
					history[i] = history[i][0] + 'CC'
				elif len(history[i]) == 3:
					history[i] = history[i][0] + 'C'
				del history[i+1]
				del history[i+1]

			else :
				change = False
		i+=1
	return history
