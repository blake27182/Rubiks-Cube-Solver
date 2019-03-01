#
#  Cube.py
#  Rubik's Cube Solver
#
#  Created by Blake Williams on 1/10/19.
#  Copyright © 2019 Blake Williams. All rights reserved.
#


import transformers
import solvers
import copy

class Cube:
	def __init__(self, u, d, l, r, f, b):
		self.faceU = copy.deepcopy(u)		#Andrew's help
		self.faceD = copy.deepcopy(d)
		self.faceL = copy.deepcopy(l)
		self.faceR = copy.deepcopy(r)
		self.faceF = copy.deepcopy(f)
		self.faceB = copy.deepcopy(b)

	history = []


	# Solving Functions

	AdjColor = solvers.AdjColor
	AdjFaceColor = solvers.AdjFaceColor
	IsSolved = solvers.IsSolved
	SqColor = solvers.SqColor
	SqFaceColor = solvers.SqFaceColor
	IsSideColor = solvers.IsSideColor
	IsCornerColor = solvers.IsCornerColor
	IsPositioned = solvers.IsPositioned
	SubSolveCount = solvers.SubSolveCount
	GetWhiteCross = solvers.GetWhiteCross
	GetWhiteCorners = solvers.GetWhiteCorners
	GetSides = solvers.GetSides
	GetYellowCross = solvers.GetYellowCross
	GetYellowCorners = solvers.GetYellowCorners
	CompleteSolve = solvers.CompleteSolve
		
	
	# Transforming Functions

	PrintList = transformers.PrintList
	PrintCube = transformers.PrintCube
	ListCopy = transformers.ListCopy
	UC  = transformers.UC 
	UCC = transformers.UCC 
	DC  = transformers.DC 
	DCC = transformers.DCC 
	LC  = transformers.LC 
	LCC = transformers.LCC 
	RC  = transformers.RC 
	RCC = transformers.RCC 
	FC  = transformers.FC 
	FCC = transformers.FCC 
	BC  = transformers.BC 
	BCC = transformers.BCC 
	XC  = transformers.XC 
	XCC = transformers.XCC 
	YC  = transformers.YC 
	YCC = transformers.YCC 
	ZC  = transformers.ZC 
	ZCC = transformers.ZCC 
	Scramble = transformers.Scramble 




