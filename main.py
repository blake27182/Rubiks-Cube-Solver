#
#  main.py
#  Rubik's Cube Solver
#
#  Created by Blake Williams on 1/10/19.
#  Copyright © 2019 Blake Williams. All rights reserved.
#


from Cube import Cube
from Transcriber import RealMovesOnly as Realify
from Transcriber import Compress
# from Piper import PrintToBot

faceU = [[0,0,0],[0,0,0],[0,0,0]]		# Initial solved cube faces
faceD = [[1,1,1],[1,1,1],[1,1,1]]
faceL = [[2,2,2],[2,2,2],[2,2,2]]
faceR = [[3,3,3],[3,3,3],[3,3,3]]
faceF = [[4,4,4],[4,4,4],[4,4,4]]
faceB = [[5,5,5],[5,5,5],[5,5,5]]


# insert bit about loading each face from the camera here

cube1 = Cube(faceU,faceD,faceL,faceR,faceF,faceB)	# Instantiation for the object
cube1.Scramble(50)				# Scrambles the cube with 50 random moves
cube1.history = []				# Resets the cube's move history to empty
cube1.PrintCube()				# Prints the faces of the scrambled cube to the console
print()

cube1.CompleteSolve()				# Solves the cube
cube1.PrintCube()					# Prints the faces of the cube 
realMoves=Realify(cube1.history)	# Removes all cube rotations from history and converts relative tranformations to absolute
print(len(realMoves))				# Prints the number of moves
print(realMoves)
realMoves=Compress(realMoves)		# Compresses moves to be more efficient
print(len(realMoves))				# Prints the number of moves
print(realMoves)


# print(realMoves)
# print(len(realMoves))
# PrintToBot(realMoves)