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


def main():
    faceU = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]		# Initial solved cube faces
    faceD = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    faceL = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    faceR = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
    faceF = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
    faceB = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]

    # insert bit about loading each face from the camera here

    cube1 = Cube(faceU, faceD, faceL, faceR, faceF, faceB)
    cube1.Scramble(50)				# Scrambles the cube with 50 random moves
    cube1.history = []				# Resets the cube's move history to empty
    print('\nScrambled Cube:\n')
    cube1.PrintCube()				# Prints the scrambled cube

    cube1.CompleteSolve()				# Solves the cube
    print('Solved Cube:\n')
    cube1.PrintCube()					# Prints the solved cube

    realMoves = Realify(cube1.history)  # Converts moves from relative to absolute
    print('\nAbsolute Moves:\n')
    print(len(realMoves))				# Prints the number of moves
    print(realMoves)
    print()

    cmpMoves = Compress(realMoves)		# Compresses moves to be more efficient
    print('\nCompressed Moves:\n')
    print(len(cmpMoves))				# Prints the number of moves
    print(cmpMoves)                     # Prints the moves

    # PrintToBot(realMoves)


if __name__ == '__main__':
    main()
