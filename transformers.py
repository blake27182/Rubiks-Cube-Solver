#
#  transformers.py
#  Rubik's Cube Solver
#
#  Created by Blake Williams on 1/10/19.
#  Copyright © 2019 Blake Williams. All rights reserved.
#


from numpy import ones_like
import random
import copy


def UC(self):
    """Transforms the cube object

    Imitates a clockwise move on the up face
    """
    temp = ones_like(self.faceU)			# top face rotation 90deg
    for y in range(3):
        for x in range(3):
            a = y
            b = -x+2
            temp[y][x] = self.faceU[b][a]
    self.faceU = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceF)		# right to front top row
    for x in range(3):
        self.faceF[0][x] = self.faceR[0][x]
    temp2 = ones_like(self.faceL)			# front to left top row
    temp2 = copy.deepcopy(self.faceL)
    for x in range(3):
        self.faceL[0][x] = temp[0][x]
    temp = copy.deepcopy(self.faceB)		# left to back top to bottom row
    for x in range(3):
        self.faceB[2][2-x] = temp2[0][x]
    for x in range(3):						# back to right bottom to top row
        self.faceR[0][2-x] = temp[2][x]
    self.history.append("UC")


def UCC(self):
    """Transforms the cube object

    Imitates a counterclockwise move on the up face
    """
    temp = ones_like(self.faceU)
    for y in range(3):
        for x in range(3):
            a = -y+2
            b = x
            temp[y][x] = self.faceU[b][a]
    self.faceU = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceF)
    for x in range(3):
        self.faceF[0][x] = self.faceL[0][x]
    temp2 = ones_like(self.faceR)
    temp2 = copy.deepcopy(self.faceR)
    for x in range(3):
        self.faceR[0][x] = temp[0][x]
    temp = copy.deepcopy(self.faceB)
    for x in range(3):
        self.faceB[2][2-x] = temp2[0][x]
    for x in range(3):
        self.faceL[0][2-x] = temp[2][x]
    self.history.append("UCC")


def DC(self):
    """Transforms the cube object

    Imitates a clockwise move on the down face
    """
    temp = ones_like(self.faceD)
    for y in range(3):
        for x in range(3):
            a = y
            b = -x+2
            temp[y][x] = self.faceD[b][a]
    self.faceD = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceR)
    for i in range(3):
        self.faceR[2][i] = self.faceF[2][i]
    temp2 = ones_like(self.faceB)
    temp2 = copy.deepcopy(self.faceB)
    for i in range(3):
        self.faceB[0][2-i] = temp[2][i]
    temp = copy.deepcopy(self.faceL)
    for i in range(3):
        self.faceL[2][i] = temp2[0][2-i]
    for i in range(3):
        self.faceF[2][i] = temp[2][i]
    self.history.append("DC")


def DCC(self):
    """Transforms the cube object

    Imitates a counterclockwise move on the down face
    """
    temp = ones_like(self.faceD)
    for y in range(3):
        for x in range(3):
            a = -y+2
            b = x
            temp[y][x] = self.faceD[b][a]
    self.faceD = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceL)
    for i in range(3):
        self.faceL[2][i] = self.faceF[2][i]
    temp2 = ones_like(self.faceB)
    temp2 = copy.deepcopy(self.faceB)
    for i in range(3):
        self.faceB[0][i] = temp[2][2-i]
    temp = copy.deepcopy(self.faceR)
    for i in range(3):
        self.faceR[2][i] = temp2[0][2-i]
    for i in range(3):
        self.faceF[2][i] = temp[2][i]
    self.history.append("DCC")


def LC(self):
    """Transforms the cube object

    Imitates a clockwise move on the left face
    """
    temp = ones_like(self.faceL)
    for y in range(3):
        for x in range(3):
            a = y
            b = -x+2
            temp[y][x] = self.faceL[b][a]
    self.faceL = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceF)
    for i in range(3):
        self.faceF[i][0] = self.faceU[i][0]
    temp2 = ones_like(self.faceD)
    temp2 = copy.deepcopy(self.faceD)
    for i in range(3):
        self.faceD[i][0] = temp[i][0]
    temp = copy.deepcopy(self.faceB)
    for i in range(3):
        self.faceB[i][0] = temp2[i][0]
    for i in range(3):
        self.faceU[i][0] = temp[i][0]
    self.history.append("LC")


def LCC(self):
    """Transforms the cube object

    Imitates a counterclockwise move on the left face
    """
    temp = ones_like(self.faceL)
    for y in range(3):
        for x in range(3):
            a = -y+2
            b = x
            temp[y][x] = self.faceL[b][a]
    self.faceL = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceB)
    for i in range(3):
        self.faceB[i][0] = self.faceU[i][0]
    temp2 = ones_like(self.faceD)
    temp2 = copy.deepcopy(self.faceD)
    for i in range(3):
        self.faceD[i][0] = temp[i][0]
    temp = copy.deepcopy(self.faceF)
    for i in range(3):
        self.faceF[i][0] = temp2[i][0]
    for i in range(3):
        self.faceU[i][0] = temp[i][0]
    self.history.append("LCC")


def RC(self):
    """Transforms the cube object

    Imitates a clockwise move on the right face
    """
    temp = ones_like(self.faceR)
    for y in range(3):
        for x in range(3):
            a = y
            b = -x+2
            temp[y][x] = self.faceR[b][a]
    self.faceR = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceB)
    for y in range(3):
        self.faceB[y][2] = self.faceU[y][2]
    temp2 = ones_like(self.faceD)
    temp2 = copy.deepcopy(self.faceD)
    for y in range(3):
        self.faceD[y][2] = temp[y][2]
    temp = copy.deepcopy(self.faceF)
    for y in range(3):
        self.faceF[y][2] = temp2[y][2]
    for y in range(3):
        self.faceU[y][2] = temp[y][2]
    self.history.append("RC")


def RCC(self):
    """Transforms the cube object

    Imitates a counterclockwise move on the right face
    """
    temp = ones_like(self.faceR)
    for y in range(3):
        for x in range(3):
            a = -y+2
            b = x
            temp[y][x] = self.faceR[b][a]
    self.faceR = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceU)
    for y in range(3):
        self.faceU[y][2] = self.faceB[y][2]
    temp2 = ones_like(self.faceF)
    temp2 = copy.deepcopy(self.faceF)
    for y in range(3):
        self.faceF[y][2] = temp[y][2]
    temp = copy.deepcopy(self.faceD)
    for y in range(3):
        self.faceD[y][2] = temp2[y][2]
    for y in range(3):
        self.faceB[y][2] = temp[y][2]
    self.history.append("RCC")


def FC(self):
    """Transforms the cube object

    Imitates a clockwise move on the front face
    """
    temp = ones_like(self.faceF)
    for y in range(3):
        for x in range(3):
            a = y
            b = -x+2
            temp[y][x] = self.faceF[b][a]
    self.faceF = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceR)
    for i in range(3):
        self.faceR[i][0] = self.faceU[2][i]
    temp2 = ones_like(self.faceR)
    temp2 = copy.deepcopy(self.faceD)
    for i in range(3):
        self.faceD[0][2-i] = temp[i][0]
    temp = copy.deepcopy(self.faceL)
    for i in range(3):
        self.faceL[i][2] = temp2[0][i]
    for i in range(3):
        self.faceU[2][i] = temp[2-i][2]
    self.history.append("FC")


def FCC(self):
    """Transforms the cube object

    Imitates a counterclockwise move on the front face
    """
    temp = ones_like(self.faceF)
    for y in range(3):
        for x in range(3):
            a = -y+2
            b = x
            temp[y][x] = self.faceF[b][a]
    self.faceF = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceL)
    for i in range(3):
        self.faceL[2-i][2] = self.faceU[2][i]
    temp2 = ones_like(self.faceD)
    temp2 = copy.deepcopy(self.faceD)
    for i in range(3):
        self.faceD[0][i] = temp[i][2]
    temp = copy.deepcopy(self.faceR)
    for i in range(3):
        self.faceR[2-i][0] = temp2[0][i]
    for i in range(3):
        self.faceU[2][i] = temp[i][0]
    self.history.append("FCC")


def BC(self):
    """Transforms the cube object

    Imitates a clockwise move on the back face
    """
    temp = ones_like(self.faceL)
    for y in range(3):
        for x in range(3):
            a = y
            b = -x+2
            temp[y][x] = self.faceB[b][a]
    self.faceB = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceL)
    for i in range(3):
        self.faceL[i][0] = self.faceU[0][2-i]
    temp2 = ones_like(self.faceD)
    temp2 = copy.deepcopy(self.faceD)
    for i in range(3):
        self.faceD[2][i] = temp[i][0]
    temp = copy.deepcopy(self.faceR)
    for i in range(3):
        self.faceR[i][2] = temp2[2][2-i]
    for i in range(3):
        self.faceU[0][i] = temp[i][2]
    self.history.append("BC")


def BCC(self):
    """Transforms the cube object

    Imitates a counterclockwise move on the back face
    """
    temp = ones_like(self.faceB)
    for y in range(3):
        for x in range(3):
            a = -y+2
            b = x
            temp[y][x] = self.faceB[b][a]
    self.faceB = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceR)
    for i in range(3):
        self.faceR[i][2] = self.faceU[0][i]
    temp2 = ones_like(self.faceD)
    temp2 = copy.deepcopy(self.faceD)
    for i in range(3):
        self.faceD[2][i] = temp[2-i][2]
    temp = copy.deepcopy(self.faceL)
    for i in range(3):
        self.faceL[i][0] = temp2[2][i]
    for i in range(3):
        self.faceU[0][i] = temp[2-i][0]
    self.history.append("BCC")


def XC(self):
    """Transforms the cube object

    Imitates rotating the cube clockwise around the x axis
    """
    temp = ones_like(self.faceR)			# right rotation 90
    for y in range(3):
        for x in range(3):
            a = y
            b = -x+2
            temp[y][x] = self.faceR[b][a]
    self.faceR = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceB)		# top to back
    self.faceB = copy.deepcopy(self.faceU)
    temp2 = ones_like(self.faceD)			# back to bottom
    temp2 = copy.deepcopy(self.faceD)
    self.faceD = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceF)		# bottom to front
    self.faceF = copy.deepcopy(temp2)
    self.faceU = copy.deepcopy(temp)		# front to top
    for y in range(3):						# left rotation 90cc
        for x in range(3):
            a = -y+2
            b = x
            temp[y][x] = self.faceL[b][a]
    self.faceL = copy.deepcopy(temp)
    self.history.append("XC")


def XCC(self):
    """Transforms the cube object

    Imitates rotating the cube counterclockwise around the x axis
    """
    temp = ones_like(self.faceR)			# right rotation 90cc
    for y in range(3):
        for x in range(3):
            a = -y+2
            b = x
            temp[y][x] = self.faceR[b][a]
    self.faceR = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceF)		# top to front
    self.faceF = copy.deepcopy(self.faceU)
    temp2 = ones_like(self.faceD)			# front to bottom
    temp2 = copy.deepcopy(self.faceD)
    self.faceD = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceB)		# bottom to back
    self.faceB = copy.deepcopy(temp2)
    self.faceU = copy.deepcopy(temp)		# back to top
    for y in range(3):						# left rotation 90
        for x in range(3):
            a = y
            b = -x+2
            temp[y][x] = self.faceL[b][a]
    self.faceL = copy.deepcopy(temp)
    self.history.append("XCC")


def YC(self):
    """Transforms the cube object

    Imitates rotating the cube clockwise around the y axis
    """
    temp = ones_like(self.faceU)			# top face rotation 90deg
    for y in range(3):
        for x in range(3):
            a = y
            b = -x+2
            temp[y][x] = self.faceU[b][a]
    self.faceU = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceL)		# front to left
    self.faceL = copy.deepcopy(self.faceF)
    temp2 = ones_like(self.faceB)			# left to back with 180deg
    temp2 = copy.deepcopy(self.faceB)
    for y in range(3):
        for x in range(3):
            self.faceB[y][x] = temp[2-y][2-x]
    temp = copy.deepcopy(self.faceR)		# back to right with 180deg
    for y in range(3):
        for x in range(3):
            self.faceR[y][x] = temp2[2-y][2-x]
    self.faceF = copy.deepcopy(temp)		# right to front
    for y in range(3):						# bottom face rotation 90deg
        for x in range(3):
            a = -y+2
            b = x
            temp[y][x] = self.faceD[b][a]
    self.faceD = copy.deepcopy(temp)
    self.history.append("YC")


def YCC(self):
    """Transforms the cube object

    Imitates rotating the cube counterclockwise around the y axis
    """
    temp = ones_like(self.faceU)
    for y in range(3):
        for x in range(3):
            a = -y+2
            b = x
            temp[y][x] = self.faceU[b][a]
    self.faceU = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceR)
    self.faceR = copy.deepcopy(self.faceF)
    temp2 = ones_like(self.faceB)
    temp2 = copy.deepcopy(self.faceB)
    for y in range(3):
        for x in range(3):
            self.faceB[y][x] = temp[2-y][2-x]
    temp = copy.deepcopy(self.faceL)
    for y in range(3):
        for x in range(3):
            self.faceL[y][x] = temp2[2-y][2-x]
    self.faceF = copy.deepcopy(temp)
    for y in range(3):
        for x in range(3):
            a = y
            b = -x+2
            temp[y][x] = self.faceD[b][a]
    self.faceD = copy.deepcopy(temp)
    self.history.append("YCC")


def ZC(self):
    """Transforms the cube object

    Imitates rotating the cube clockwise around the z axis
    """
    temp = ones_like(self.faceF)			# front rotation 90
    for y in range(3):
        for x in range(3):
            a = y
            b = -x+2
            temp[y][x] = self.faceF[b][a]
    self.faceF = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceR)		# top to right with 90cc
    for y in range(3):
        for x in range(3):
            a = -y+2
            b = x
            self.faceR[y][x] = self.faceU[b][a]
    temp2 = ones_like(self.faceD)			# right to bottom with 90cc
    temp2 = copy.deepcopy(self.faceD)
    for y in range(3):
        for x in range(3):
            a = -y+2
            b = x
            self.faceD[y][x] = temp[b][a]
    temp = copy.deepcopy(self.faceL)		# bottom to left with 90cc
    for y in range(3):
        for x in range(3):
            a = -y+2
            b = x
            self.faceL[y][x] = temp2[b][a]
    for y in range(3):						# left to top with 90cc
        for x in range(3):
            a = -y+2
            b = x
            self.faceU[y][x] = temp[b][a]
    for y in range(3):						# back rotation 90cc
        for x in range(3):
            a = -y+2
            b = x
            temp[y][x] = self.faceB[b][a]
    self.faceB = copy.deepcopy(temp)
    self.history.append("ZC")


def ZCC(self):
    """Transforms the cube object

    Imitates rotating the cube counterclockwise around the z axis
    """
    temp = ones_like(self.faceF)			# front rotation 90
    for y in range(3):
        for x in range(3):
            a = -y+2
            b = x
            temp[y][x] = self.faceF[b][a]
    self.faceF = copy.deepcopy(temp)
    temp = copy.deepcopy(self.faceL)		# top to left with 90
    for y in range(3):
        for x in range(3):
            a = y
            b = -x + 2
            self.faceL[y][x] = self.faceU[b][a]
    temp2 = ones_like(self.faceD)			# left to bottom with 90
    temp2 = copy.deepcopy(self.faceD)
    for y in range(3):
        for x in range(3):
            a = y
            b = -x+2
            self.faceD[y][x] = temp[b][a]
    temp = copy.deepcopy(self.faceR)		# bottom to right with 90
    for y in range(3):
        for x in range(3):
            a = y
            b = -x+2
            self.faceR[y][x] = temp2[b][a]
    for y in range(3):						# right to top with 90
        for x in range(3):
            a = y
            b = -x+2
            self.faceU[y][x] = temp[b][a]
    for y in range(3):						# back rotation 90
        for x in range(3):
            a = y
            b = -x+2
            temp[y][x] = self.faceB[b][a]
    self.faceB = copy.deepcopy(temp)
    self.history.append("ZCC")


def Scramble(self, number):
    """Scrambles the Cube for testing purposes

    Args:
        number (int): number of moves to make while scrambling
    """
    possibilities = [
        "UC", "UCC", "DC", "DCC", "LC", "LCC",
        "RC", "RCC", "FC", "FCC", "BC", "BCC"
    ]
    choices = []
    for i in range(number):			# fills a list of random choices from the list of possibilities
        choices.append(random.choice(possibilities))
    for i in choices:				# executes each move in the list of choices
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