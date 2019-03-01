#
#  solvers.py
#  Rubik's Cube Solver
#
#  Created by Blake Williams on 1/10/19.
#  Copyright © 2019 Blake Williams. All rights reserved.
#


import copy
import time

# average move-count: 178

def AdjColor(self,face,row,col,axis):
	tempCube = copy.deepcopy(self)					#Turning the tempCube to face front
	if (face=='U'):
		tempCube.XCC()
	elif(face=='D'):								
		tempCube.XC()
	elif(face=='L'):
		tempCube.YCC()
	elif(face=='R'):
		tempCube.YC()
	elif(face=='F'):
		pass
	elif(face=='B'):
		tempCube.XCC()
		tempCube.XCC()
	else:
		print("Error AdjColor: invalid face")

	if (axis=='Y'):									#Selecting an adjacent square
		newCol = col
		if (row==0):
			newRow = 2
			return tempCube.faceU[newRow][newCol]
		elif(row==2):
			newRow = 0
			return tempCube.faceD[newRow][newCol]
	elif (axis=='X'):
		newRow = row
		if (col==0):
			newCol = 2
			return tempCube.faceL[newRow][newCol]
		elif (col==2):
			newCol = 0
			return tempCube.faceR[newRow][newCol]

def AdjFaceColor(self,face,row,col,axis):
	tempCube = copy.deepcopy(self)
	if (face=='U'):
		tempCube.XCC()
	elif(face=='D'):
		tempCube.XC()
	elif(face=='L'):
		tempCube.YCC()
	elif(face=='R'):
		tempCube.YC()
	elif(face=='F'):
		pass
	elif(face=='B'):
		tempCube.XCC()
		tempCube.XCC()
	else:
		print("Error AdjColor: invalid face")

	if (axis=='Y'):
		if (row==0):
			return tempCube.faceU[1][1]
		elif(row==2):
			return tempCube.faceD[1][1]
	elif (axis=='X'):
		if (col==0):
			return tempCube.faceL[1][1]
		elif (col==2):
			return tempCube.faceR[1][1]

def SqColor(self,face,row,col):
	if (face=='U'):
		return self.faceU[row][col]
	elif(face=='D'):
		return self.faceD[row][col]
	elif(face=='L'):
		return self.faceL[row][col]
	elif(face=='R'):
		return self.faceR[row][col]
	elif(face=='F'):
		return self.faceF[row][col]
	elif(face=='B'):
		return self.faceB[row][col]

def SqFaceColor(self,face):
	if (face=='U'):
		return self.faceU[1][1]
	elif(face=='D'):
		return self.faceD[1][1]
	elif(face=='L'):
		return self.faceL[1][1]
	elif(face=='R'):
		return self.faceR[1][1]
	elif(face=='F'):
		return self.faceF[1][1]
	elif(face=='B'):
		return self.faceB[1][1]

def IsSideColor(self,face,color):						# Returns bool for if given color exists as a side piece on given face
	if (face=='U'):
		return self.faceU[0][1]==color or self.faceU[1][0]==color or self.faceU[1][2]==color or self.faceU[2][1]==color
	if (face=='D'):
		return self.faceD[0][1]==color or self.faceD[1][0]==color or self.faceD[1][2]==color or self.faceD[2][1]==color
	if (face=='L'):
		return self.faceL[0][1]==color or self.faceL[1][0]==color or self.faceL[1][2]==color or self.faceL[2][1]==color
	if (face=='R'):
		return self.faceR[0][1]==color or self.faceR[1][0]==color or self.faceR[1][2]==color or self.faceR[2][1]==color
	if (face=='F'):
		return self.faceF[0][1]==color or self.faceF[1][0]==color or self.faceF[1][2]==color or self.faceF[2][1]==color
	if (face=='B'):
		return self.faceB[0][1]==color or self.faceB[1][0]==color or self.faceB[1][2]==color or self.faceB[2][1]==color

def IsCornerColor(self,face,color):				# Returns bool for if given color exists as a corner piece on given face
	if (face=='U'):
		return self.faceU[0][0]==color or self.faceU[0][2]==color or self.faceU[2][0]==color or self.faceU[2][2]==color
	if (face=='D'):
		return self.faceD[0][0]==color or self.faceD[0][2]==color or self.faceD[2][0]==color or self.faceD[2][2]==color
	if (face=='L'):
		return self.faceL[0][0]==color or self.faceL[0][2]==color or self.faceL[2][0]==color or self.faceL[2][2]==color
	if (face=='R'):
		return self.faceR[0][0]==color or self.faceR[0][2]==color or self.faceR[2][0]==color or self.faceR[2][2]==color
	if (face=='F'):
		return self.faceF[0][0]==color or self.faceF[0][2]==color or self.faceF[2][0]==color or self.faceF[2][2]==color
	if (face=='B'):
		return self.faceB[0][0]==color or self.faceB[0][2]==color or self.faceB[2][0]==color or self.faceB[2][2]==color

def IsSolved(self,face,row,col):
	xAxisCheck = self.AdjColor(face,row,col,'X')==self.AdjFaceColor(face,row,col,'X')		#Andrew's help
	yAxisCheck = self.AdjColor(face,row,col,'Y')==self.AdjFaceColor(face,row,col,'Y')
	sameFaceCheck = self.SqColor(face,row,col)==self.SqFaceColor(face)
	return xAxisCheck and yAxisCheck and sameFaceCheck

def IsPositioned(self,face,row,col):
	cornerColors = []
	cornerColors.append(self.AdjFaceColor(face,row,col,'X'))
	cornerColors.append(self.AdjFaceColor(face,row,col,'Y'))
	cornerColors.append(self.SqFaceColor(face))
	xAxisCheck = self.AdjColor(face,row,col,'X') in cornerColors
	yAxisCheck = self.AdjColor(face,row,col,'Y') in cornerColors
	sameFaceCheck = self.SqColor(face,row,col) in cornerColors
	return xAxisCheck and yAxisCheck and sameFaceCheck

def SubSolveCount(self):
	count = 0
	if self.IsSolved('U',0,1):
		count+=1
	if self.IsSolved('U',1,0):
		count+=1
	if self.IsSolved('U',1,2):
		count+=1
	if self.IsSolved('U',2,1):
		count+=1
	return count

def GetWhiteCross(self):
	start = time.time()
	while not (self.IsSolved('U',0,1) and self.IsSolved('U',1,0) and self.IsSolved('U',1,2) and self.IsSolved('U',2,1)):  
																					# while the cross is not solved
		if time.time()-start>2:
			raise Exception("infinite loop")
		if (self.faceU[0][1]==0):					# move whites on top that arent solved
			if(not self.IsSolved('U',0,1)):				# needs to loop at least once before function end
				self.BCC()
		if (self.faceU[1][0]==0):
			if(not self.IsSolved('U',1,0)):
				self.LCC()
		if (self.faceU[1][2]==0):
			if(not self.IsSolved('U',1,2)):
				self.RCC()
		if (self.faceU[2][1]==0):
			if(not self.IsSolved('U',2,1)):
				self.FCC()

		while self.IsSideColor('F',0) or self.IsSideColor('R',0) or self.IsSideColor('B',0) or self.IsSideColor('L',0):
			if time.time()-start>2:
				raise Exception("infinite loop")
			if (self.IsSideColor('F',0)):				# If theres a white on the front face...
				while (self.faceF[1][2] != 0):		# move white square to the right position
					if time.time()-start>2:
						raise Exception("infinite loop")
					self.FC()

				self.RCC()							# move piece to bottom with white facing down
				self.DCC()
				self.RC()

				while self.faceF[1][1] != self.faceF[2][1]:	# move the bottom face until it matches middle
					if time.time()-start>2:
						raise Exception("infinite loop")
					self.DC()
					self.YC()

				self.FC()							# finish piece solve by moving to the top
				self.FC()

			else:
				self.YC()

		if self.IsSideColor('D',0):
			while self.faceD[0][1] != 0:
				if time.time()-start>2:
					raise Exception("infinite loop")
				self.YC()							# turn cube until white square on bottom face is on top

			while self.faceF[1][1] != self.faceF[2][1]:	# move the bottom face until it matches middle
				if time.time()-start>2:
					raise Exception("infinite loop")
				self.DC()
				self.YC()

			self.FC()								# finish piece solve by moving to the top
			self.FC()

def GetWhiteCorners(self):
	start = time.time()
	while not (self.IsSolved('U',0,0) and self.IsSolved('U',0,2) and self.IsSolved('U',2,0) and self.IsSolved('U',2,2)):
		if time.time()-start>2:
			raise Exception("infinite loop")
		for i in range(4):								# solve bottom right corner on top if positioned 
			if self.IsPositioned('F',2,2):
				while not self.IsSolved('F',2,2):
					if time.time()-start>2:
						raise Exception("infinite loop")
					self.RCC()
					self.DCC()
					self.RC()
					self.DC()
			elif self.faceU[2][2]==0:					# move if not positioned and white
				self.RCC()
				self.DCC()
				self.RC() 
				self.DC()
			self.YC()

		while self.IsCornerColor('F',0) or self.IsCornerColor('R',0) or self.IsCornerColor('B',0) or self.IsCornerColor('L',0):
			if time.time()-start>2:
				raise Exception("infinite loop")
			if self.IsCornerColor('F',0):
				if self.faceF[0][0] == 0:				# move white corner to bottom row
					self.FCC()
					self.DCC()
					self.FC()
					self.DC()
				elif self.faceF[0][2] == 0:
					self.FC()
					self.DC()
					self.FCC()
					self.DCC()

				if self.faceF[2][0] == 0:				# solve corner on left side
					while self.AdjColor('F',2,0,'X') != self.AdjFaceColor('F',2,0,'X'):
						if time.time()-start>2:
							raise Exception("infinite loop")
						self.DC()
						self.YC()
					self.YCC()
					self.RCC()
					self.DCC()
					self.RC()
					self.DC()	

				if self.faceF[2][2] == 0:				# solve corner on right side
					while self.AdjColor('F',2,2,'X') != self.AdjFaceColor('F',2,2,'X'):
						if time.time()-start>2:
							raise Exception("infinite loop")
						self.DC()
						self.YC()
					self.YC()
					self.LC()
					self.DC()
					self.LCC()
					self.DCC()

			else:
				self.YC()

		if self.IsCornerColor('D',0):
			while self.faceD[0][2] != 0:
				if time.time()-start>2:
					raise Exception("infinite loop")
				self.YC()
			while self.AdjColor('D',0,2,'X') != self.AdjFaceColor('D',0,2,'Y'):
				if time.time()-start>2:
					raise Exception("infinite loop")
				self.YC()
				self.DC()
			while not self.IsSolved('U',2,2):
				if time.time()-start>2:
					raise Exception("infinite loop")
				self.RCC()
				self.DCC()
				self.RC()
				self.DC()

def GetSides(self):
	start = time.time()
	while not(self.IsSolved('F',1,0) and self.IsSolved('F',1,2) and self.IsSolved('B',1,0) and self.IsSolved('B',1,2)):
		if time.time()-start>2:
			raise Exception("infinite loop")
		frontLeft = self.faceF[1][0]==1 or self.faceL[1][2]==1
		frontRight = self.faceF[1][2]==1 or self.faceR[1][0]==1
		backLeft = self.faceB[1][0]==1 or self.faceL[1][0]==1
		backRight = self.faceB[1][2]==1 or self.faceR[1][2]==1
		middleHasYellow = frontLeft or frontRight or backLeft or backRight
		if not middleHasYellow:								# if all yellows are on top
			while self.IsSolved('F',1,2):
				if time.time()-start>2:
					raise Exception("infinite loop")
				self.YC()
			self.UC()										# move a yellow down to the right into an unsolved spot
			self.RC()
			self.UCC()
			self.RCC()
			self.UCC()
			self.FCC()
			self.UC()
			self.FC()
		else:
			while self.SqColor('F',0,1)==1 or self.AdjColor('F',0,1,'Y')==1:		# rotate the cube until the top middle piece has no yellow
				if time.time()-start>2:
					raise Exception("infinite loop")
				self.YC()
			while self.SqColor('F',0,1)!=self.SqFaceColor('F'):			# rotate bottom two layers until top middle matches front face
				if time.time()-start>2:
					raise Exception("infinite loop")
				self.UCC()
				self.YC()
			if self.AdjColor('F',0,1,'Y') == self.SqFaceColor('L'):		# if top middle piece matches space to the left, solve it
				self.UCC()										
				self.LCC()
				self.UC()
				self.LC()
				self.UC()
				self.FC()
				self.UCC()
				self.FCC()
			elif self.AdjColor('F',0,1,'Y') == self.SqFaceColor('R'):		# if top middle piece matches space to the right, solve it
				self.UC()										
				self.RC()
				self.UCC()
				self.RCC()
				self.UCC()
				self.FCC()
				self.UC()
				self.FC()

def GetYellowCross(self):
	start = time.time()
	while not(self.faceU[0][1]==1 and self.faceU[1][0]==1 and self.faceU[1][2]==1 and self.faceU[2][1]==1):
		if time.time()-start>2:
			raise Exception("infinite loop")
		if self.IsSideColor('U',1):												# perform algorithm until all top sides are yellow
			while not (self.faceU[2][1]!=1 and self.faceU[1][0]==1):		# move cube so that the cross or bar or square is in position
				if time.time()-start>2:
					raise Exception("infinite loop")
				self.YC()
			self.FC()
			self.RC()
			self.UC()
			self.RCC()
			self.UCC()
			self.FCC()
		else:
			self.FC()
			self.RC()
			self.UC()
			self.RCC()
			self.UCC()
			self.FCC()

	while not(self.IsSolved('U',0,1) and self.IsSolved('U',1,0) and self.IsSolved('U',1,2) and self.IsSolved('U',2,1)):
		if time.time()-start>2:
			raise Exception("infinite loop")
		if self.SubSolveCount()>=2:
			while not (self.IsSolved('U',1,2) and not self.IsSolved('U',2,1)):
				if time.time()-start>2:
					raise Exception("infinite loop")
				self.YCC()
			self.RC()												
			self.UC()
			self.RCC()
			self.UC()
			self.RC()
			self.UC()
			self.UC()
			self.RCC()
			self.UC()
		else:
			self.UC()

def GetYellowCorners(self):
	start = time.time()
	while not (self.IsPositioned('U',0,0) or self.IsPositioned('U',0,2) or self.IsPositioned('U',2,0) or self.IsPositioned('U',2,2)):
		if time.time()-start>2:
			raise Exception("infinite loop")
		self.UC()											# perform algorithm until at least one corner is positioned
		self.RC()
		self.UCC()
		self.LCC()
		self.UC()
		self.RCC()
		self.UCC()
		self.LC()											

	while not self.IsPositioned('U',2,2):						# move cube until bottom right on top is positioned
		if time.time()-start>2:
			raise Exception("infinite loop")
		self.YC()

	while not (self.IsPositioned('U',0,0) and self.IsPositioned('U',0,2) and self.IsPositioned('U',2,0) and self.IsPositioned('U',2,2)):
		if time.time()-start>2:
			raise Exception("infinite loop")
		self.UC()											# perform algorithm until all corners are positioned
		self.RC()
		self.UCC()
		self.LCC()
		self.UC()
		self.RCC()
		self.UCC()
		self.LC()

	for i in range(4):										# perform algorithm for each corner until yellow faces up
		while self.faceU[2][2]!=1:
			if time.time()-start>2:
				raise Exception("infinite loop")
			self.RCC()
			self.DCC()
			self.RC()
			self.DC()
		self.UCC()

	while not self.IsSolved('U',0,0):
		if time.time()-start>2:
			raise Exception("infinite loop")
		self.UCC()

def CompleteSolve(self):
	self.GetWhiteCross()
	self.GetWhiteCorners()
	self.ZC()
	self.ZC()
	self.GetSides()
	self.GetYellowCross()
	self.GetYellowCorners()