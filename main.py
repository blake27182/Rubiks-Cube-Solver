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
# import Piper

faceU = [[0,0,0],[0,0,0],[0,0,0]]
faceD = [[1,1,1],[1,1,1],[1,1,1]]
faceL = [[2,2,2],[2,2,2],[2,2,2]]
faceR = [[3,3,3],[3,3,3],[3,3,3]]
faceF = [[4,4,4],[4,4,4],[4,4,4]]
faceB = [[5,5,5],[5,5,5],[5,5,5]]


cube1 = Cube(faceU,faceD,faceL,faceR,faceF,faceB)
cube1.Scramble(50)
cube1.history = []
cube1.PrintCube()
print()

cube1.CompleteSolve()
cube1.PrintCube()
realMoves=Realify(cube1.history)
print(len(realMoves))
realMoves=Compress(realMoves)
print(len(realMoves))


# print(realMoves)
# print(len(realMoves))
# Piper.Log(realMoves)