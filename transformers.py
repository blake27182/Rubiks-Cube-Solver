#
#  transformers.py
#  Rubik's Cube Solver
#
#  Created by Blake Williams on 1/10/19.
#  Copyright © 2019 Blake Williams. All rights reserved.
#


from numpy import ones_like
import random

def PrintList(self, li, name="none"):
	n=0
	for i in li:
		if(n!=1):
			print(i)
		else:
			print(i,name)
		n+=1
	print()

def PrintCube(self):
	self.PrintList(self.faceU,"U")
	self.PrintList(self.faceD,"D")
	self.PrintList(self.faceL,"L")
	self.PrintList(self.faceR,"R")
	self.PrintList(self.faceF,"F")
	self.PrintList(self.faceB,"B")

def ListCopy(self,lito,lifrom):
	for y in range(3):
		for x in range(3):
			lito[y][x] = lifrom[y][x]

def UC(self):
	temp = ones_like(self.faceU)			#top face rotation 90deg
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2	
			temp[y][x]=self.faceU[b][a]
	self.ListCopy(self.faceU,temp)
	self.ListCopy(temp,self.faceF)			#right to front top row
	for x in range(3):
		self.faceF[0][x] = self.faceR[0][x]
	temp2 = ones_like(self.faceL)			#front to left top row
	self.ListCopy(temp2,self.faceL)
	for x in range(3):
		self.faceL[0][x] = temp[0][x]
	self.ListCopy(temp,self.faceB)			#left to back top to bottom row
	for x in range(3):
		self.faceB[2][2-x] = temp2[0][x]
	for x in range(3):						#back to right bottom to top row
		self.faceR[0][2-x] = temp[2][x]
	self.history.append("UC")

def UCC(self):
	temp = ones_like(self.faceU)
	for y in range(3):
		for x in range(3):
			a=-y+2
			b=x	
			temp[y][x]=self.faceU[b][a]
	self.ListCopy(self.faceU,temp)
	self.ListCopy(temp,self.faceF)
	for x in range(3):
		self.faceF[0][x] = self.faceL[0][x]
	temp2 = ones_like(self.faceR)
	self.ListCopy(temp2,self.faceR)
	for x in range(3):
		self.faceR[0][x] = temp[0][x]
	self.ListCopy(temp,self.faceB)
	for x in range(3):
		self.faceB[2][2-x] = temp2[0][x]
	for x in range(3):
		self.faceL[0][2-x] = temp[2][x]
	self.history.append("UCC")

def DC(self):
	temp = ones_like(self.faceD)
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2
			temp[y][x]=self.faceD[b][a]
	self.ListCopy(self.faceD,temp)
	self.ListCopy(temp,self.faceR)
	for i in range(3):
		self.faceR[2][i] = self.faceF[2][i]
	temp2 = ones_like(self.faceB)
	self.ListCopy(temp2,self.faceB)
	for i in range(3):
		self.faceB[0][2-i] = temp[2][i]
	self.ListCopy(temp,self.faceL)
	for i in range(3):
		self.faceL[2][i] = temp2[0][2-i]
	for i in range(3):
		self.faceF[2][i] = temp[2][i]
	self.history.append("DC")

def DCC(self):
	temp = ones_like(self.faceD)
	for y in range(3):
		for x in range(3):
			a=-y+2
			b=x	
			temp[y][x]=self.faceD[b][a]
	self.ListCopy(self.faceD,temp)
	self.ListCopy(temp,self.faceL)
	for i in range(3):
		self.faceL[2][i] = self.faceF[2][i]
	temp2 = ones_like(self.faceB)
	self.ListCopy(temp2,self.faceB)
	for i in range(3):
		self.faceB[0][i] = temp[2][2-i]
	self.ListCopy(temp,self.faceR)
	for i in range(3):
		self.faceR[2][i] = temp2[0][2-i]
	for i in range(3):
		self.faceF[2][i] = temp[2][i]
	self.history.append("DCC")

def LC(self):
	temp = ones_like(self.faceL)
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2
			temp[y][x]=self.faceL[b][a]
	self.ListCopy(self.faceL,temp)
	self.ListCopy(temp,self.faceF)
	for i in range(3):
		self.faceF[i][0] = self.faceU[i][0]
	temp2 = ones_like(self.faceD)
	self.ListCopy(temp2,self.faceD)
	for i in range(3):
		self.faceD[i][0] = temp[i][0]
	self.ListCopy(temp,self.faceB)
	for i in range(3):
		self.faceB[i][0] = temp2[i][0]
	for i in range(3):
		self.faceU[i][0] = temp[i][0]
	self.history.append("LC")

def LCC(self):
	temp = ones_like(self.faceL)
	for y in range(3):
		for x in range(3):
			a=-y+2
			b=x	
			temp[y][x]=self.faceL[b][a]
	self.ListCopy(self.faceL,temp)
	self.ListCopy(temp,self.faceB)
	for i in range(3):
		self.faceB[i][0] = self.faceU[i][0]
	temp2 = ones_like(self.faceD)
	self.ListCopy(temp2,self.faceD)
	for i in range(3):
		self.faceD[i][0] = temp[i][0]
	self.ListCopy(temp,self.faceF)
	for i in range(3):
		self.faceF[i][0] = temp2[i][0]
	for i in range(3):
		self.faceU[i][0] = temp[i][0]
	self.history.append("LCC")

def RC(self):
	temp = ones_like(self.faceR)
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2	
			temp[y][x]=self.faceR[b][a]
	self.ListCopy(self.faceR,temp)
	self.ListCopy(temp,self.faceB)
	for y in range(3):
		self.faceB[y][2] = self.faceU[y][2]
	temp2 = ones_like(self.faceD)
	self.ListCopy(temp2,self.faceD)
	for y in range(3):
		self.faceD[y][2] = temp[y][2]
	self.ListCopy(temp,self.faceF)
	for y in range(3):
		self.faceF[y][2] = temp2[y][2]
	for y in range(3):
		self.faceU[y][2] = temp[y][2]
	self.history.append("RC")

def RCC(self):
	temp = ones_like(self.faceR)
	for y in range(3):
		for x in range(3):
			a=-y+2
			b=x
			temp[y][x]=self.faceR[b][a]
	self.ListCopy(self.faceR,temp)
	self.ListCopy(temp,self.faceU)
	for y in range(3):
		self.faceU[y][2] = self.faceB[y][2]
	temp2 = ones_like(self.faceF)
	self.ListCopy(temp2,self.faceF)
	for y in range(3):
		self.faceF[y][2] = temp[y][2]
	self.ListCopy(temp,self.faceD)
	for y in range(3):
		self.faceD[y][2] = temp2[y][2]
	for y in range(3):
		self.faceB[y][2] = temp[y][2]
	self.history.append("RCC")

def FC(self):
	temp = ones_like(self.faceF)
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2
			temp[y][x]=self.faceF[b][a]
	self.ListCopy(self.faceF,temp)
	self.ListCopy(temp,self.faceR)
	for i in range(3):
		self.faceR[i][0] = self.faceU[2][i]
	temp2 = ones_like(self.faceR)
	self.ListCopy(temp2,self.faceD)
	for i in range(3):
		self.faceD[0][2-i] = temp[i][0]
	self.ListCopy(temp,self.faceL)
	for i in range(3):
		self.faceL[i][2] = temp2[0][i]
	for i in range(3):
		self.faceU[2][i] = temp[2-i][2]
	self.history.append("FC")

def FCC(self):
	temp = ones_like(self.faceF)
	for y in range(3):
		for x in range(3):
			a=-y+2
			b=x	
			temp[y][x]=self.faceF[b][a]
	self.ListCopy(self.faceF,temp)
	self.ListCopy(temp,self.faceL)
	for i in range(3):
		self.faceL[2-i][2] = self.faceU[2][i]
	temp2 = ones_like(self.faceD)
	self.ListCopy(temp2,self.faceD)
	for i in range(3):
		self.faceD[0][i] = temp[i][2]
	self.ListCopy(temp,self.faceR)
	for i in range(3):
		self.faceR[2-i][0] = temp2[0][i]
	for i in range(3):
		self.faceU[2][i] = temp[i][0]
	self.history.append("FCC")

def BC(self):
	temp = ones_like(self.faceL)
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2
			temp[y][x]=self.faceB[b][a]
	self.ListCopy(self.faceB,temp)
	self.ListCopy(temp,self.faceL)
	for i in range(3):
		self.faceL[i][0] = self.faceU[0][2-i]
	temp2 = ones_like(self.faceD)
	self.ListCopy(temp2,self.faceD)
	for i in range(3):
		self.faceD[2][i] = temp[i][0]
	self.ListCopy(temp,self.faceR)
	for i in range(3):
		self.faceR[i][2] = temp2[2][2-i]
	for i in range(3):
		self.faceU[0][i] = temp[i][2]
	self.history.append("BC")

def BCC(self):
	temp = ones_like(self.faceB)
	for y in range(3):
		for x in range(3):
			a=-y+2
			b=x	
			temp[y][x]=self.faceB[b][a]
	self.ListCopy(self.faceB,temp)
	self.ListCopy(temp,self.faceR)
	for i in range(3):
		self.faceR[i][2] = self.faceU[0][i]
	temp2 = ones_like(self.faceD)
	self.ListCopy(temp2,self.faceD)
	for i in range(3):
		self.faceD[2][i] = temp[2-i][2]
	self.ListCopy(temp,self.faceL)
	for i in range(3):
		self.faceL[i][0] = temp2[2][i]
	for i in range(3):
		self.faceU[0][i] = temp[2-i][0]
	self.history.append("BCC")

def XC(self):
	temp = ones_like(self.faceR)			#right rotation 90
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2
			temp[y][x]=self.faceR[b][a]
	self.ListCopy(self.faceR,temp)
	self.ListCopy(temp,self.faceB)			#top to back					
	self.ListCopy(self.faceB,self.faceU)
	temp2 = ones_like(self.faceD)			#back to bottom
	self.ListCopy(temp2,self.faceD)
	self.ListCopy(self.faceD,temp)	
	self.ListCopy(temp,self.faceF)			#bottom to front
	self.ListCopy(self.faceF,temp2)	
	self.ListCopy(self.faceU,temp)			#front to top
	for y in range(3):						#left rotation 90cc
		for x in range(3):
			a=-y+2
			b=x	
			temp[y][x]=self.faceL[b][a]
	self.ListCopy(self.faceL,temp)
	self.history.append("XC")

def XCC(self):
	temp = ones_like(self.faceR)			#right rotation 90cc
	for y in range(3):
		for x in range(3):
			a=-y+2
			b=x
			temp[y][x]=self.faceR[b][a]
	self.ListCopy(self.faceR,temp)
	self.ListCopy(temp,self.faceF)			#top to front					
	self.ListCopy(self.faceF,self.faceU)
	temp2 = ones_like(self.faceD)			#front to bottom
	self.ListCopy(temp2,self.faceD)
	self.ListCopy(self.faceD,temp)	
	self.ListCopy(temp,self.faceB)			#bottom to back
	self.ListCopy(self.faceB,temp2)	
	self.ListCopy(self.faceU,temp)			#back to top
	for y in range(3):						#left rotation 90
		for x in range(3):
			a=y
			b=-x+2	
			temp[y][x]=self.faceL[b][a]
	self.ListCopy(self.faceL,temp)
	self.history.append("XCC")

def YC(self):
	temp = ones_like(self.faceU)			#top face rotation 90deg
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2
			temp[y][x]=self.faceU[b][a]
	self.ListCopy(self.faceU,temp)
	self.ListCopy(temp,self.faceL)			#front to left
	self.ListCopy(self.faceL,self.faceF)
	temp2 = ones_like(self.faceB)			#left to back with 180deg
	self.ListCopy(temp2,self.faceB)
	for y in range(3):
		for x in range(3):
			self.faceB[y][x] = temp[2-y][2-x]
	self.ListCopy(temp,self.faceR)			#back to right with 180deg
	for y in range(3):
		for x in range(3):
			self.faceR[y][x] = temp2[2-y][2-x]
	self.ListCopy(self.faceF,temp)			#right to front
	for y in range(3):						#bottom face rotation 90deg
		for x in range(3):
			a=-y+2
			b=x	
			temp[y][x] = self.faceD[b][a]
	self.ListCopy(self.faceD,temp)
	self.history.append("YC")

def YCC(self):
	temp = ones_like(self.faceU)
	for y in range(3):
		for x in range(3):
			a=-y+2
			b=x	
			temp[y][x]=self.faceU[b][a]
	self.ListCopy(self.faceU,temp)
	self.ListCopy(temp,self.faceR)
	self.ListCopy(self.faceR,self.faceF)
	temp2 = ones_like(self.faceB)
	self.ListCopy(temp2,self.faceB)
	for y in range(3):
		for x in range(3):
			self.faceB[y][x] = temp[2-y][2-x]
	self.ListCopy(temp,self.faceL)
	for y in range(3):
		for x in range(3):
			self.faceL[y][x] = temp2[2-y][2-x]
	self.ListCopy(self.faceF,temp)
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2
			temp[y][x]=self.faceD[b][a]
	self.ListCopy(self.faceD,temp)
	self.history.append("YCC")

def ZC(self):
	temp = ones_like(self.faceF)			#front rotation 90
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2
			temp[y][x]=self.faceF[b][a]
	self.ListCopy(self.faceF,temp)
	self.ListCopy(temp,self.faceR)			#top to right with 90cc
	for y in range(3):
		for x in range(3):
			a=-y+2
			b=x	
			self.faceR[y][x]=self.faceU[b][a]
	temp2 = ones_like(self.faceD)			#right to bottom with 90cc
	self.ListCopy(temp2,self.faceD)
	for y in range(3):
		for x in range(3):
			a=-y+2
			b=x	
			self.faceD[y][x]=temp[b][a]		
	self.ListCopy(temp,self.faceL)			#bottom to left with 90cc
	for y in range(3):
		for x in range(3):
			a=-y+2
			b=x	
			self.faceL[y][x]=temp2[b][a]		
	for y in range(3):						#left to top with 90cc
		for x in range(3):
			a=-y+2
			b=x	
			self.faceU[y][x] = temp[b][a]
	for y in range(3):						#back rotation 90cc
		for x in range(3):
			a=-y+2
			b=x	
			temp[y][x]=self.faceB[b][a]
	self.ListCopy(self.faceB,temp)
	self.history.append("ZC")

def ZCC(self):
	temp = ones_like(self.faceF)			#front rotation 90
	for y in range(3):
		for x in range(3):
			a=-y+2
			b=x
			temp[y][x]=self.faceF[b][a]
	self.ListCopy(self.faceF,temp)
	self.ListCopy(temp,self.faceL)			#top to left with 90
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2
			self.faceL[y][x]=self.faceU[b][a]
	temp2 = ones_like(self.faceD)			#left to bottom with 90
	self.ListCopy(temp2,self.faceD)
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2
			self.faceD[y][x]=temp[b][a]		
	self.ListCopy(temp,self.faceR)			#bottom to right with 90
	for y in range(3):
		for x in range(3):
			a=y
			b=-x+2
			self.faceR[y][x]=temp2[b][a]		
	for y in range(3):						#right to top with 90
		for x in range(3):
			a=y
			b=-x+2	
			self.faceU[y][x] = temp[b][a]
	for y in range(3):						#back rotation 90
		for x in range(3):
			a=y
			b=-x+2
			temp[y][x]=self.faceB[b][a]
	self.ListCopy(self.faceB,temp)
	self.history.append("ZCC")

def Scramble(self,number):
	possibilities = ["UC","UCC","DC","DCC","LC","LCC","RC","RCC","FC","FCC","BC","BCC"]
	choices = []
	for i in range(number):
		choices.append(random.choice(possibilities))
	for i in choices:
		if i == "UC":
			self.UC()
		elif i == "UCC":
			self.UCC()
		elif i == "DC":
			self.DC()
		elif i == "DCC":
			self.DCC()
		elif i == "LC":
			self.LC()
		elif i == "LCC":
			self.LCC()
		elif i == "RC":
			self.RC()
		elif i == "RCC":
			self.RCC()
		elif i == "FC":
			self.FC()
		elif i == "FCC":
			self.FCC()
		elif i == "BC":
			self.BC()
		elif i == "BCC":
			self.BCC()