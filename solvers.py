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


def AdjColor(self, face, row, col, axis):
    """Gets the value (color) of an adjacent square

    Does not accept center squares

    Args:
        face (str): Face on cube
        row (int): Row on face
        col (int): Column on face
        axis (str): 'Y' or 'X'

    Returns:
        (int): Value (color) of the adjacent square
    """
    tempCube = copy.deepcopy(self)					# Turning the tempCube to face front
    if face == 'U':
        tempCube.XCC()
    elif face == 'D':
        tempCube.XC()
    elif face == 'L':
        tempCube.YCC()
    elif face == 'R':
        tempCube.YC()
    elif face == 'F':
        pass
    elif face == 'B':
        tempCube.XCC()
        tempCube.XCC()
    else:
        print("Error AdjColor: invalid face")

    if axis == 'Y':									#Selecting an adjacent square based on axis and position
        newCol = col
        if row == 0:
            newRow = 2
            return tempCube.faceU[newRow][newCol]
        elif row == 2:
            newRow = 0
            return tempCube.faceD[newRow][newCol]
    elif axis == 'X':
        newRow = row
        if col == 0:
            newCol = 2
            return tempCube.faceL[newRow][newCol]
        elif col == 2:
            newCol = 0
            return tempCube.faceR[newRow][newCol]


def AdjFaceColor(self, face, row, col, axis):
    """Gets the value (color) of the adjacent face

    Does not accept center squares

    Args:
        face (str): Face on cube
        row (int): Row on face
        col (int): Column on face
        axis (str): 'Y' or 'X'

    Returns:
        (int): Value (color) of the adjacent center square
    """
    tempCube = copy.deepcopy(self)
    if face == 'U':
        tempCube.XCC()
    elif face == 'D':
        tempCube.XC()
    elif face == 'L':
        tempCube.YCC()
    elif face == 'R':
        tempCube.YC()
    elif face == 'F':
        pass
    elif face == 'B':
        tempCube.XCC()
        tempCube.XCC()
    else:
        print("Error AdjColor: invalid face")

    if axis == 'Y':
        if row == 0:
            return tempCube.faceU[1][1]
        elif row == 2:
            return tempCube.faceD[1][1]
    elif axis == 'X':
        if col == 0:
            return tempCube.faceL[1][1]
        elif col == 2:
            return tempCube.faceR[1][1]


def SqColor(self, face, row, col):
    """Gets the value (color) of a square (useful when face is unknown)

    Args:
        face (str): Face on cube
        row (int): Row on face
        col (int): Column on face

    Returns:
        (int): Value (color) of the square
    """
    if face == 'U':
        return self.faceU[row][col]
    elif face == 'D':
        return self.faceD[row][col]
    elif face == 'L':
        return self.faceL[row][col]
    elif face == 'R':
        return self.faceR[row][col]
    elif face == 'F':
        return self.faceF[row][col]
    elif face == 'B':
        return self.faceB[row][col]


def SqFaceColor(self, face):
    """Gets the value of the center square on any given face

    Args:
        face (str): Face on cube

    Returns:
        (int): The value (color) of the center square
    """
    if face == 'U':
        return self.faceU[1][1]
    elif face == 'D':
        return self.faceD[1][1]
    elif face == 'L':
        return self.faceL[1][1]
    elif face == 'R':
        return self.faceR[1][1]
    elif face == 'F':
        return self.faceF[1][1]
    elif face == 'B':
        return self.faceB[1][1]


def IsSideColor(self, face, color):
    """Decides if the given color exists as a side piece on the given face

    Args:
        face (str): Face on cube
        color (int): Color value in question

    Returns:
        (bool): True if the color is present, False if not
    """
    if face == 'U':
        return (self.faceU[0][1] == color
                or self.faceU[1][0] == color
                or self.faceU[1][2] == color
                or self.faceU[2][1] == color)
    if face == 'D':
        return (self.faceD[0][1] == color
                or self.faceD[1][0] == color
                or self.faceD[1][2] == color
                or self.faceD[2][1] == color)
    if face == 'L':
        return (self.faceL[0][1] == color
                or self.faceL[1][0] == color
                or self.faceL[1][2] == color
                or self.faceL[2][1] == color)
    if face == 'R':
        return (self.faceR[0][1] == color
                or self.faceR[1][0] == color
                or self.faceR[1][2] == color
                or self.faceR[2][1] == color)
    if face == 'F':
        return (self.faceF[0][1] == color
                or self.faceF[1][0] == color
                or self.faceF[1][2] == color
                or self.faceF[2][1] == color)
    if face == 'B':
        return (self.faceB[0][1] == color
                or self.faceB[1][0] == color
                or self.faceB[1][2] == color
                or self.faceB[2][1] == color)


def IsCornerColor(self, face, color):
    """Decides if given color exists as a corner piece on given face

    Args:
        face (str): Face on cube
        color (int): Color value in question

    Returns:
        (bool): True if the color is present, False if it is not
    """
    if face == 'U':
        return (self.faceU[0][0] == color
                or self.faceU[0][2] == color
                or self.faceU[2][0] == color
                or self.faceU[2][2] == color)
    if face == 'D':
        return (self.faceD[0][0] == color
                or self.faceD[0][2] == color
                or self.faceD[2][0] == color
                or self.faceD[2][2] == color)
    if face == 'L':
        return (self.faceL[0][0] == color
                or self.faceL[0][2] == color
                or self.faceL[2][0] == color
                or self.faceL[2][2] == color)
    if face == 'R':
        return (self.faceR[0][0] == color
                or self.faceR[0][2] == color
                or self.faceR[2][0] == color
                or self.faceR[2][2] == color)
    if face == 'F':
        return (self.faceF[0][0] == color
                or self.faceF[0][2] == color
                or self.faceF[2][0] == color
                or self.faceF[2][2] == color)
    if face == 'B':
        return (self.faceB[0][0] == color
                or self.faceB[0][2] == color
                or self.faceB[2][0] == color
                or self.faceB[2][2] == color)


def IsSolved(self, face, row, col):
    """Decides if the piece the given square is on is solved

    Args:
        face (str): Face on cube
        row (int): Row on face
        col (int): Column on face

    Returns:
        (bool): True if it is solved, False if not
    """
    xAxisCheck = self.AdjColor(face, row, col, 'X') \
        == self.AdjFaceColor(face, row, col, 'X')

    yAxisCheck = self.AdjColor(face, row, col, 'Y') \
        == self.AdjFaceColor(face, row, col, 'Y')

    sameFaceCheck = self.SqColor(face, row, col) == self.SqFaceColor(face)
    return xAxisCheck and yAxisCheck and sameFaceCheck


def IsPositioned(self, face, row, col):
    """Decides if the piece the given square is on is in the right place

    Args:
        face (str): Face on cube
        row (int): Row on face
        col (int): Column on face

    Returns:
        (bool): True if the piece is position
    """
    cornerColors = [
        self.AdjFaceColor(face, row, col, 'X'),
        self.AdjFaceColor(face, row, col, 'Y'),
        self.SqFaceColor(face),
    ]

    xAxisCheck = self.AdjColor(face, row, col, 'X') in cornerColors
    yAxisCheck = self.AdjColor(face, row, col, 'Y') in cornerColors
    sameFaceCheck = self.SqColor(face, row, col) in cornerColors
    return xAxisCheck and yAxisCheck and sameFaceCheck


def SubSolveCount(self):
    """Counts the number of side pieces that are solved on the top face

    Returns:
        (int): Number of solved pieces (max: 4)
    """
    count = 0
    if self.IsSolved('U', 0, 1):
        count += 1
    if self.IsSolved('U', 1, 0):
        count += 1
    if self.IsSolved('U', 1, 2):
        count += 1
    if self.IsSolved('U', 2, 1):
        count += 1
    return count


def GetWhiteCross(self):
    """The first major step in solving

    Solves all four side pieces on the top
    """
    start = time.time()				# while loop safe catch
    while not (self.IsSolved('U', 0, 1)
               and self.IsSolved('U', 1, 0)
               and self.IsSolved('U', 1, 2)
               and self.IsSolved('U', 2, 1)):
        # while the cross is not solved
        if time.time()-start > 2:
            raise Exception("infinite loop")

        if self.faceU[0][1] == 0 and not self.IsSolved('U', 0, 1):					# move whites on top that arent solved
            self.BCC()																# needs to loop at least once before function end
        if self.faceU[1][0] == 0 and not self.IsSolved('U', 1, 0):
            self.LCC()
        if self.faceU[1][2] == 0 and not self.IsSolved('U', 1, 2):
            self.RCC()
        if self.faceU[2][1] == 0 and not self.IsSolved('U', 2, 1):		# if this piece is white and not solved
            self.FCC()													# move it off the top face

        while (self.IsSideColor('F', 0)
               or self.IsSideColor('R', 0)
               or self.IsSideColor('B', 0)
               or self.IsSideColor('L', 0)):
            # while there is a white side square somewhere on the side faces
            if time.time()-start > 2:
                raise Exception("infinite loop")
            if self.IsSideColor('F', 0):				# If there's a white on the front face...
                while self.faceF[1][2] != 0:			# move white square to the right position
                    if time.time()-start > 2:
                        raise Exception("infinite loop")
                    self.FC()

                self.RCC()							# move piece to bottom with white facing down
                self.DCC()
                self.RC()

                while self.faceF[1][1] != self.faceF[2][1]:		# move the bottom face until the bottom front square matches middle
                    if time.time()-start > 2:
                        raise Exception("infinite loop")
                    self.DC()
                    self.YC()

                self.FC()							# finish piece solve by moving it to the top
                self.FC()

            else:			# there are no white squares on the front, rotate the cube
                self.YC()

        if self.IsSideColor('D', 0):			# if there is a white side square on the bottom face
            while self.faceD[0][1] != 0:
                if time.time()-start > 2:
                    raise Exception("infinite loop")
                self.YC()							# rotate the cube until white square on bottom face is in the top position

            while self.faceF[1][1] != self.faceF[2][1]:	# move the bottom face until the adjacent color matches the adjacent middle
                if time.time()-start > 2:
                    raise Exception("infinite loop")
                self.DC()
                self.YC()

            self.FC()								# finish piece solve by moving to the top
            self.FC()


def GetWhiteCorners(self):
    """Second major step in solving

    Solve all four corner pieces on the top
    """
    start = time.time()				# while loop safe catch
    while not (self.IsSolved('U', 0, 0)
               and self.IsSolved('U', 0, 2)
               and self.IsSolved('U', 2, 0)
               and self.IsSolved('U', 2, 2)):

        if time.time()-start > 2:
            raise Exception("infinite loop")
        for i in range(4):								# solve bottom right corner on top if positioned correctly
            if self.IsPositioned('F',2,2):
                while not self.IsSolved('F',2,2):
                    if time.time()-start > 2:
                        raise Exception("infinite loop")
                    self.RCC()
                    self.DCC()
                    self.RC()
                    self.DC()
            elif self.faceU[2][2] == 0:					# move to bottom layer if white but not in poisition
                self.RCC()
                self.DCC()
                self.RC()
                self.DC()
            self.YC()

        while self.IsCornerColor('F', 0) \
                or self.IsCornerColor('R', 0) \
                or self.IsCornerColor('B', 0) \
                or self.IsCornerColor('L', 0):
            # while there is a white corner square somewhere on the side faces
            if time.time()-start > 2:
                raise Exception("infinite loop")
            if self.IsCornerColor('F', 0):
                if self.faceF[0][0] == 0:				# move white corner to bottom row if on top row
                    self.FCC()
                    self.DCC()
                    self.FC()
                    self.DC()
                elif self.faceF[0][2] == 0:				# move white corner to bottom row if on top row
                    self.FC()
                    self.DC()
                    self.FCC()
                    self.DCC()

                if self.faceF[2][0] == 0:				# solve corner on left side bottom row
                    while (self.AdjColor('F', 2, 0, 'X')
                           != self.AdjFaceColor('F', 2, 0, 'X')):
                        if time.time()-start > 2:
                            raise Exception("infinite loop")
                        self.DC()
                        self.YC()
                    self.YCC()
                    self.RCC()
                    self.DCC()
                    self.RC()
                    self.DC()

                if self.faceF[2][2] == 0:				# solve corner on right side bottom row
                    while (self.AdjColor('F', 2, 2, 'X')
                           != self.AdjFaceColor('F', 2, 2, 'X')):

                        if time.time()-start > 2:
                            raise Exception("infinite loop")
                        self.DC()
                        self.YC()
                    self.YC()
                    self.LC()
                    self.DC()
                    self.LCC()
                    self.DCC()

            else:				# if there is no white corner square on the front, rotate the cube
                self.YC()

        if self.IsCornerColor('D', 0):		# if there is a white corner square on the bottom face
            while self.faceD[0][2] != 0:		# rotate the cube until it is in the top right position
                if time.time()-start > 2:
                    raise Exception("infinite loop")
                self.YC()
            while (self.AdjColor('D', 0, 2, 'X')
                   != self.AdjFaceColor('D', 0, 2, 'Y')):		# move the bottom face until the piece is directly
                if time.time()-start > 2:												#	below its solved position
                    raise Exception("infinite loop")
                self.YC()
                self.DC()
            while not self.IsSolved('U', 2, 2):			# solve the peice
                if time.time()-start > 2:
                    raise Exception("infinite loop")
                self.RCC()
                self.DCC()
                self.RC()
                self.DC()


def GetSides(self):
    """Third major step in solving

    Solve the middle layer
    """
    start = time.time()				# while loop safe catch
    while not(self.IsSolved('F', 1, 0)
              and self.IsSolved('F', 1, 2)
              and self.IsSolved('B', 1, 0)
              and self.IsSolved('B', 1, 2)):

        if time.time()-start > 2:
            raise Exception("infinite loop")
        frontLeft = self.faceF[1][0] == 1 or self.faceL[1][2] == 1		# breaking up conditional for if the middle layer contains a yellow square
        frontRight = self.faceF[1][2] == 1 or self.faceR[1][0] == 1
        backLeft = self.faceB[1][0] == 1 or self.faceL[1][0] == 1
        backRight = self.faceB[1][2] == 1 or self.faceR[1][2] == 1
        middleHasYellow = frontLeft or frontRight or backLeft or backRight
        if not middleHasYellow:								# if all yellow side squares are on top layer (previously the bottom layer)
            while self.IsSolved('F', 1, 2):
                if time.time()-start > 2:
                    raise Exception("infinite loop")
                self.YC()									# rotate the cube until the middle right piece is one that is not solved
            self.UC()										# move a yellow down to the right into an unsolved spot
            self.RC()
            self.UCC()
            self.RCC()
            self.UCC()
            self.FCC()
            self.UC()
            self.FC()
        else:
            while (self.SqColor('F', 0, 1) == 1
                   or self.AdjColor('F', 0, 1, 'Y') == 1):		# rotate the cube until the top middle piece has no yellow
                if time.time()-start > 2:
                    raise Exception("infinite loop")
                self.YC()
            while self.SqColor('F', 0, 1) != self.SqFaceColor('F'):			# move bottom two layers until top middle square matches front face
                if time.time()-start > 2:
                    raise Exception("infinite loop")
                self.UCC()
                self.YC()
            if self.AdjColor('F', 0, 1, 'Y') == self.SqFaceColor('L'):		# if top middle piece goes in the space to the left, solve it
                self.UCC()
                self.LCC()
                self.UC()
                self.LC()
                self.UC()
                self.FC()
                self.UCC()
                self.FCC()
            elif self.AdjColor('F', 0, 1, 'Y') == self.SqFaceColor('R'):		# if top middle piece goes in the space to the right, solve it
                self.UC()
                self.RC()
                self.UCC()
                self.RCC()
                self.UCC()
                self.FCC()
                self.UC()
                self.FC()


def GetYellowCross(self):
    """Fourth major step in solving

    Solves all four side pieces on the bottom (now top) layer
    """
    start = time.time()				# while loop safe catch
    while not(self.faceU[0][1] == 1
              and self.faceU[1][0] == 1
              and self.faceU[1][2] == 1
              and self.faceU[2][1] == 1):

        # while not all the side squares on the top are yellow
        if time.time()-start > 2:
            raise Exception("infinite loop")
        if self.IsSideColor('U', 1):				# if there is a yellow side square on the top
            while not (self.faceU[2][1] != 1 and self.faceU[1][0] == 1):
                if time.time()-start > 2:
                    raise Exception("infinite loop")
                self.YC()		    # rotate the cube until there is a yellow square to the right and not one on the bottom
            self.FC()			# perform an algorithm to change the formation of yellow squares on the top
            self.RC()
            self.UC()
            self.RCC()
            self.UCC()
            self.FCC()
        else:					# if there are no yellow side squares on the top
            self.FC()			# perform the algorithm without rotating the cube first, as in the first case
            self.RC()
            self.UC()
            self.RCC()
            self.UCC()
            self.FCC()

    while not(self.IsSolved('U', 0, 1)
              and self.IsSolved('U', 1, 0)
              and self.IsSolved('U', 1, 2)
              and self.IsSolved('U', 2, 1)):

        # while not all side pieces on top are solved
        if time.time()-start > 2:
            raise Exception("infinite loop")
        if self.SubSolveCount() >= 2:							# if there is more than 1 yellow piece solved on top
            while not (self.IsSolved('U', 1, 2)
                       and not self.IsSolved('U', 2, 1)):		# rotate the cube until the piece to the right is
                if time.time()-start > 2:					    #	solved but not the piece to the bottom
                    raise Exception("infinite loop")
                self.YCC()
            self.RC()			# perform an algorithm that switches the two pieces to left and bottom
            self.UC()
            self.RCC()
            self.UC()
            self.RC()
            self.UC()
            self.UC()
            self.RCC()
            self.UC()
        else:					# if there are fewer than 2 solved yellow pieces, move the top layer to possibly
            self.UC()			#	expose one of the pieces to a solved position


def GetYellowCorners(self):
    """Fifth major step in solving

    Solve all four corner pieces on yellow face (now top)
    """
    start = time.time()				# while loop safe catch
    while not (self.IsPositioned('U', 0, 0)
               or self.IsPositioned('U', 0, 2)
               or self.IsPositioned('U', 2, 0)
               or self.IsPositioned('U', 2, 2)):
        # while none of the top corners are positioned
        if time.time()-start > 2:
            raise Exception("infinite loop")
        self.UC()									# perform algorithm that switches top right, top left and bottom left pieces in rotation
        self.RC()
        self.UCC()
        self.LCC()
        self.UC()
        self.RCC()
        self.UCC()
        self.LC()

    while not self.IsPositioned('U', 2, 2):						# rotate cube until bottom right piece on top is positioned
        if time.time()-start > 2:
            raise Exception("infinite loop")
        self.YC()

    while not (self.IsPositioned('U', 0, 0)
               and self.IsPositioned('U', 0, 2)
               and self.IsPositioned('U', 2, 0)
               and self.IsPositioned('U', 2, 2)):

        # while not all corner pieces are in correct position
        if time.time()-start > 2:
            raise Exception("infinite loop")
        self.UC()									# perform algorithm that switches top right, top left and bottom left pieces in rotation
        self.RC()
        self.UCC()
        self.LCC()
        self.UC()
        self.RCC()
        self.UCC()
        self.LC()

    for i in range(4):								# perform algorithm that rotates corner pieces for each corner until each is solved
        while self.faceU[2][2] != 1:				#	by this point, all four corner pieces should be positioned correctly
            if time.time()-start > 2:
                raise Exception("infinite loop")
            self.RCC()
            self.DCC()
            self.RC()
            self.DC()
        self.UCC()

    while not self.IsSolved('U', 0, 0):		# move top layer until the top left corner is solved (resulting in all four corners being solved)
        if time.time()-start > 2:
            raise Exception("infinite loop")
        self.UCC()


def CompleteSolve(self):
    """Parent function to the solver functions

    Assuming the given cube is possible to solve, this will solve it completely
    """
    self.GetWhiteCross()
    self.GetWhiteCorners()
    self.ZC()					# rotates the cube so that the bottom face is now the top face, accomidating the proceeding functions that
    self.ZC()					# assume this rotation has taken place. This makes the algorithms and conditionals easier to visualize
    self.GetSides()
    self.GetYellowCross()
    self.GetYellowCorners()
